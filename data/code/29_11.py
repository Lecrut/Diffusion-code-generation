def reverse_word(s):
    return s[::-1]
if __name__ == '__main__':
    test_string1 = "hello"
    result1 = reverse_word(test_string1)
    print(f"'{test_string1}' reversed is '{result1}'")
    test_string2 = "world"
    result2 = reverse_word(test_string2)
    print(f"'{test_string2}' reversed is '{result2}'")
    test_string3 = "Python"
    result3 = reverse_word(test_string3)
    print(f"'{test_string3}' reversed is '{result3}'")