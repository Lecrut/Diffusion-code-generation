def find_string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
if __name__ == '__main__':
    test_string1 = "hello"
    result1 = find_string_length(test_string1)
    print(result1)
    test_string2 = ""
    result2 = find_string_length(test_string2)
    print(result2)
    test_string3 = "Python"
    result3 = find_string_length(test_string3)
    print(result3)
    test_string4 = "1234567890"
    result4 = find_string_length(test_string4)
    print(result4)