def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    SAMPLE_STRING_1 = "hello"
    SAMPLE_STRING_2 = "world"
    SAMPLE_STRING_3 = "Python"

    reversed_string_1 = reverse_string(SAMPLE_STRING_1)
    reversed_string_2 = reverse_string(SAMPLE_STRING_2)
    reversed_string_3 = reverse_string(SAMPLE_STRING_3)

    print(f"Original: {SAMPLE_STRING_1}, Reversed: {reversed_string_1}")
    print(f"Original: {SAMPLE_STRING_2}, Reversed: {reversed_string_2}")
    print(f"Original: {SAMPLE_STRING_3}, Reversed: {reversed_string_3}")