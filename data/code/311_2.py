def reverse_string(s):
    return s[::-1]
if __name__ == '__main__':
    test_string = "hello"
    reversed_str = reverse_string(test_string)
    print(reversed_str)
    test_string_2 = "world"
    reversed_str_2 = reverse_string(test_string_2)
    print(reversed_str_2)
    test_string_3 = "Python"
    reversed_str_3 = reverse_string(test_string_3)
    print(reversed_str_3)