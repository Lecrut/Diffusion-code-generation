def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def count_characters(text):
    validate_input(text)
    return sum(1 for _ in text)

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Python",
        "OpenAI",
        "",
        "1234567890"
    ]
    for text in sample_texts:
        print(count_characters(text))