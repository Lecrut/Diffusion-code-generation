def reverse_string(s):
    return s[::-1]
if __name__ == '__main__':
    test_string_1 = "hello"
    reversed_1 = reverse_string(test_string_1)
    print(f"Original: {test_string_1}, Reversed: {reversed_1}")
    test_string_2 = "world"
    reversed_2 = reverse_string(test_string_2)
    print(f"Original: {test_string_2}, Reversed: {reversed_2}")
    test_string_3 = "optimization"
    reversed_3 = reverse_string(test_string_3)
    print(f"Original: {test_string_3}, Reversed: {reversed_3}")
    test_string_4 = ""
    reversed_4 = reverse_string(test_string_4)
    print(f"Original: {test_string_4}, Reversed: {reversed_4}")