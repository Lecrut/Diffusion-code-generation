import sys

def process_string(input_str: str) -> None:
    """Takes a string, prints it as-is, fully capitalized, and title-cased."""
    print(input_str)
    print(input_str.upper())
    # Title case logic that handles multiple spaces correctly by splitting on whitespace
    words = input_str.split()
    if not words:
        title_cased = ""
    else:
        title_cased = " ".join(word.capitalize() for word in words)
    print(title_cased)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements, no user input or arguments needed.
    test_cases = [
        "hello world",
        "this is a python script example!",
        "",  # edge case: empty string
        "   multiple spaces here   ",
    ]

    for test_input in test_cases:
        process_string(test_input)