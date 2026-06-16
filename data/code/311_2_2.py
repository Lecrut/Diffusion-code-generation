def reverse_string(s):
    return s[::-1]
if __name__ == '__main__':
    test_string1 = "hello"
    reversed_string1 = reverse_string(test_string1)
    print(f"Original: {test_string1}, Reversed: {reversed_string1}")
    test_string2 = "world"
    reversed_string2 = reverse_string(test_string2)
    print(f"Original: {test_string2}, Reversed: {reversed_string2}")
    test_string3 = "Python"
    reversed_string3 = reverse_string(test_string3)
    print(f"Original: {test_string3}, Reversed: {reversed_string3}")