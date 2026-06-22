def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def count_characters(text):
    validate_input(text)
    return sum(1 for char in text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(count_characters(sample_text))