def extract_unique_characters(text):
    unique_chars = set()
    ordered_chars = []
    for char in text:
        if char not in unique_chars:
            unique_chars.add(char)
            ordered_chars.append(char)
    return ordered_chars

if __name__ == '__main__':
    sample_text1 = "Hello World"
    sample_text2 = "Python programming is great!"
    print(extract_unique_characters(sample_text1))
    print(extract_unique_characters(sample_text2))