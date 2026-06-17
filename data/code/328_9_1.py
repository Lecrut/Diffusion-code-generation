def find_string_length(s):
    count = 0
    for char in s:
        count = count + 1
    return count
if __name__ == '__main__':
    test_string1 = "hello"
    result1 = find_string_length(test_string1)
    print(f"The length of '{test_string1}' is: {result1}")
    test_string2 = "world"
    result2 = find_string_length(test_string2)
    print(f"The length of '{test_string2}' is: {result2}")
    test_string3 = ""
    result3 = find_string_length(test_string3)
    print(f"The length of '{test_string3}' is: {result3}")
    test_string4 = "Python"
    result4 = find_string_length(test_string4)
    print(f"The length of '{test_string4}' is: {result4}")