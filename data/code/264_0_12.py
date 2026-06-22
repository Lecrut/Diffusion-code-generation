def validate_input(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input must be a non-empty string")

def find_words(text):
    validate_input(text)
    return text.split()

if __name__ == '__main__':
    sample_text = "Hello world this is a test"
    print(find_words(sample_text))