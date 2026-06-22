def count_characters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return sum(1 for _ in text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(count_characters(sample_text))