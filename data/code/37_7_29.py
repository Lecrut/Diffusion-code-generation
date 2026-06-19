def combine_strings(str1, str2):
    SEPARATOR = " "
    return str1 + SEPARATOR + str2

if __name__ == '__main__':
    SAMPLE_STRING_1 = "Hello"
    SAMPLE_STRING_2 = "World"
    result = combine_strings(SAMPLE_STRING_1, SAMPLE_STRING_2)
    print(result)