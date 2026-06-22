def find_repeated_chars(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    return [char for char in seen if char in repeated]

if __name__ == '__main__':
    test_string = "programming"
    result = find_repeated_chars(test_string)
    print(result)