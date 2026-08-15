import sqlite3


# Create database and FAQ table
def create_database():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    faq_data = [
        (
            "hello",
            "Hello! How can I help you?"
        ),
        (
            "hi",
            "Hi! Welcome to our chatbot."
        ),
        (
            "what are your support hours",
            "Our support team is available from 9 AM to 6 PM."
        ),
        (
            "how can I contact support",
            "You can contact our support team through email or phone."
        ),
        (
            "how can I reset my password",
            "Go to the login page and click 'Forgot Password' to reset your password."
        ),
        (
            "what payment methods do you accept",
            "We accept credit cards, debit cards and online payments."
        ),
        (
            "thank you",
            "You're welcome! Have a great day!"
        ),
        (
            "bye",
            "Goodbye! Thank you for using our chatbot."
        )
    ]

    # Remove old data to avoid duplicate questions
    cursor.execute("DELETE FROM faq")

    cursor.executemany(
        "INSERT INTO faq (question, answer) VALUES (?, ?)",
        faq_data
    )

    conn.commit()
    conn.close()


# Get answer from database
def get_response(user_input):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    user_input = user_input.lower().strip()

    cursor.execute(
        "SELECT answer FROM faq WHERE question = ?",
        (user_input,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return "Sorry, I don't understand that question."


# Run chatbot
def chatbot():
    print("===================================")
    print("       AI CUSTOMER SUPPORT CHATBOT")
    print("===================================")
    print("Type 'bye' to exit.")
    print()

    while True:
        user_input = input("You: ")

        response = get_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() == "bye":
            break


# Main program
if __name__ == "__main__":
    create_database()
    chatbot()