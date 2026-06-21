def count_characters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return sum(1 for _ in text)

if __name__ == '__main__':
    sample_texts = [
        "Hello, World!",
        "Python",
        "OpenAI",
        "",
        "1234567890"
    ]
    
    for sample_text in sample_texts:
        print(f"'{sample_text}': {count_characters(sample_text)}")