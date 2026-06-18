import sys

def get_first_letter_of_word(word: str) -> str:
    """Returns the first alphabetic character of a word, handling punctuation."""
    cleaned = ''.join(char.lower() if char.isalpha() else '' for char in word)
    return cleaned[0] if cleaned else ""

if __name__ == '__main__':
    sample_text = "Hello World\nThis is Python.\nIt works great!"

    # Split text into words based on whitespace (handles newlines automatically)
    raw_words = sample_text.split()

    output_lines = []
    for word in raw_words:
        first_char = get_first_letter_of_word(word)
        if first_char:
            output_lines.append(first_char)

    # Print each letter separated by a newline to match standard "one per line" expectation
    print('\n'.join(output_lines))