import sys

def convert_text(text: str) -> dict[str, str]:
    """
    Convert input string to lowercase, uppercase, and title case.

    Args:
        text (str): The original string to be converted.

    Returns:
        dict: A dictionary containing the three variations of the text.
            Keys are 'lower', 'upper', and 'title'.
    """
    result = {
        "lower": text.lower(),
        "upper": text.upper(),
        "title": text.title()
    }
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid input() or command-line args.
    samples = ["Hello, World!", "Python is Awesome", "A B C"]

    for sample in samples:
        converted_data = convert_text(sample)
        
        print(f"Original Input (if provided): '{sample}'")  # Label since no actual input here
        print("Conversion Results:")
        print(f"- Lowercase: {converted_data['lower']}")
        print("- Uppercase: {0}\n".format(converted_data['upper']))
        print("- Title Case:", converted_data['title'])