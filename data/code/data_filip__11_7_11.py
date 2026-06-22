def find_repeated_characters(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return ''.join(sorted(repeated))

if __name__ == '__main__':
    sample_string = "hello world"
    result = find_repeated_characters(sample_string)
    print(result)