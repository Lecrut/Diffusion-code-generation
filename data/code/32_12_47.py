def count_characters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return sum(1 for char in text)

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