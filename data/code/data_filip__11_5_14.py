def find_repeated_chars(text):
    seen = set()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    result = []
    seen = set()
    for char in text:
        if char in repeated and char not in seen:
            result.append(char)
            seen.add(char)
    return result

if __name__ == '__main__':
    sample_text = "programming"
    repeated_chars = find_repeated_chars(sample_text)
    print(repeated_chars)