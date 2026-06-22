def extract_unique_chars(phrase):
    unique_chars = set()
    for char in phrase:
        if char.isalpha():
            unique_chars.add(char)
    sorted_chars = ''.join(sorted(unique_chars))
    return sorted_chars

if __name__ == '__main__':
    sample_phrase = "hello world"
    result = extract_unique_chars(sample_phrase)
    print(result)