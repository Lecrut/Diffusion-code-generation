def has_distinct_characters(text):
    seen = {}
    for char in text:
        seen[char] = seen.get(char, 0) + 1
    for count in seen.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    test_string = "abcde"
    result = has_distinct_characters(test_string)
    print(result)
    
    test_string2 = "hello"
    result2 = has_distinct_characters(test_string2)
    print(result2)