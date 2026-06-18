import sys

def get_first_letter_of_words(text: str) -> list[str]:
    """Extracts the first letter of each word from the input text."""
    words = text.split()
    return [word[0] if word else "" for word in words]

if __name__ == '__main__':
    sample_text = (
        "Hello World\n"
        "This is a multi-line example.\n"
        "Python handles input efficiently."
    )

    result = get_first_letter_of_words(sample_text)
    print("".join(result))