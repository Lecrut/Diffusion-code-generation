def find_string_length(input_string):
    return len(input_string)
if __name__ == '__main__':
    test_string1 = "hello"
    result1 = find_string_length(test_string1)
    print(f"The length of '{test_string1}' is: {result1}")
    test_string2 = ""
    result2 = find_string_length(test_string2)
    print(f"The length of '{test_string2}' is: {result2}")
    test_string3 = "Python"
    result3 = find_string_length(test_string3)
    print(f"The length of '{test_string3}' is: {result3}")