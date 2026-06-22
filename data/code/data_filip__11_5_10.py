def find_repeated_chars(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    
    result = []
    seen_result = set()
    for char in s:
        if char in repeated and char not in seen_result:
            result.append(char)
            seen_result.add(char)
    
    return result

if __name__ == '__main__':
    test_string = "programming"
    result = find_repeated_chars(test_string)
    print(result)