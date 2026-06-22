def find_repeated_characters(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    for char in s:
        if char in repeated:
            repeated.add(char)
    return list(repeated)

if __name__ == '__main__':
    sample_string = "programming"
    result = find_repeated_characters(sample_string)
    print(result)