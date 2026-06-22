def extract_first_letters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters

if __name__ == '__main__':
    sample_values = [
        "Hello world",
        "",
        "   \t ",
        "Single",
        "  Test case ",
        "One   two   three",
        "Hello, world!",
        "123 456 789"
    ]
    
    for value in sample_values:
        try:
            print(extract_first_letters(value))
        except ValueError as e:
            print(e)