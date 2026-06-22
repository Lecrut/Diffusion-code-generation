def extract_unique_characters(phrase):
    unique_chars = set()
    result = []
    for char in phrase:
        if char not in unique_chars:
            unique_chars.add(char)
            result.append(char)
    return result

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(extract_unique_characters(sample_phrase))