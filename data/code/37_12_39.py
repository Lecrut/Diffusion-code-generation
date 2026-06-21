def combine_strings(str1, str2):
    return ''.join([str1, str2])

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "World"
    result = combine_strings(sample_str1, sample_str2)
    print(result)