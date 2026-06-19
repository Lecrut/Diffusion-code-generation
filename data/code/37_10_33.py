def concatenate_strings(string1, string2):
    SEPARATOR = " "
    return f"{string1}{SEPARATOR}{string2}"

if __name__ == '__main__':
    sample_string1 = "Hello"
    sample_string2 = "World"
    result = concatenate_strings(sample_string1, sample_string2)
    print(result)