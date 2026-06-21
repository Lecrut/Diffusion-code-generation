def concatenate_strings(str1, str2):
    SEPARATOR = " "
    return f"{str1}{SEPARATOR}{str2}"

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "World"
    result = concatenate_strings(sample_str1, sample_str2)
    print(result)