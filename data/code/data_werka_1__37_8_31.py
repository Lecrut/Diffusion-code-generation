def combine_strings(str1, str2):
    return ''.join([str1, str2])

if __name__ == '__main__':
    sample_str1 = "Hello"
    sample_str2 = "World"
    combined_result = combine_strings(sample_str1, sample_str2)
    print(combined_result)

    another_sample_str1 = "Python"
    another_sample_str2 = "Programming"
    another_combined_result = combine_strings(another_sample_str1, another_sample_str2)
    print(another_combined_result)