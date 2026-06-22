def find_repeated_characters(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    result = []
    for char in s:
        if char in repeated and char not in result:
            result.append(char)
    return result

if __name__ == '__main__':
    sample_string = "programming"
    repeated_chars = find_repeated_characters(sample_string)
    print(repeated_chars)