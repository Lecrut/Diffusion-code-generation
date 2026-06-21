def count_characters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    char_count = 0
    for _ in text:
        char_count += 1
    return char_count

if __name__ == '__main__':
    sample_text = "Alibaba Cloud"
    print(count_characters(sample_text))