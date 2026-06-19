def reverse_word(word):
    return ''.join(reversed(word))

if __name__ == '__main__':
    SAMPLE_STRING_1 = "hello"
    SAMPLE_STRING_2 = "Python"
    SAMPLE_STRING_3 = "world"

    reversed_string_1 = reverse_word(SAMPLE_STRING_1)
    reversed_string_2 = reverse_word(SAMPLE_STRING_2)
    reversed_string_3 = reverse_word(SAMPLE_STRING_3)

    print(reversed_string_1)
    print(reversed_string_2)
    print(reversed_string_3)