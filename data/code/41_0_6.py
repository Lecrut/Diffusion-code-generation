# Script to convert a string to lowercase, uppercase, and title case

def process_string(text: str) -> tuple[str, str, str]:
    """Converts input text to three different cases."""
    lower_case = text.lower()
    upper_case = text.upper()
    title_case = text.title()
    return (lower_case, upper_case, title_case)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_text = "Hello World! Python 3.10"

    lower_result, upper_result, title_result = process_string(sample_text)

    print(f"Original: {sample_text}")
    print(f"Lowercase: {lower_result}")
    print(f"Uppercase: {upper_result}")
    print(f"title Case: {title_result}")