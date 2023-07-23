# import dependencies
import requests
from simple_chalk import chalk
import pyfiglet

# for pdf saving file
import inquirer
from fpdf import FPDF

# Function to get book names by author name
def get_books_by_author(author):
    url = f"https://openlibrary.org/search.json?author={author}"
    response = requests.get(url)
    data = response.json()
    books = []
    if "docs" in data:
        for doc in data["docs"]:
            if "title" in doc:
                books.append(doc["title"])
    return books

# Save to PDF function
def save_to_pdf(author_name, books):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200,10, f"List of books by {author_name}")
    for book in books:
        pdf.cell(200,10,book)
    pdf.output(f"{author_name}_books.pdf")


# Main Function
def main():
    # printing welcome message with ASCII art
    print(chalk.green(pyfiglet.figlet_format("Books Search")))
    # Ask for author's name
    author_name = input(chalk.yellow("Please Enter the author name: "))
    books = get_books_by_author(author_name)
    # Print the book names
    if len(books) > 0:
        print(chalk.green(f"\nHere are the books by {author_name}"))
        for book in books:
            print(chalk.blue(book))
        # Ask the user to save in PDF or not
        questions = [inquirer.Confirm('save_to_pdf', message='Do you want to save the book list to PDF ?')]
        answers = inquirer.prompt(questions)
        # If user wants to save -> invoke the save_to_pdf function
        if answers['save_to_pdf']:
            save_to_pdf(author_name, books)
            print(chalk.green('\nThe book list has been saved to a PDF file.'))
    else:
        print(chalk.red(f"No books found for {author_name}"))

if __name__ == "__main__":
    main()