def find_repeated_chars(text):
    seen = set()
    repeated = set()
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    result = []
    for char in text:
        if char in repeated and char not in result:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "programming"
    repeated_chars = find_repeated_chars(sample_text)
    print(repeated_chars)