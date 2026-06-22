def concatenate_strings(str1, str2):
    SEPARATOR = " "
    return str1 + SEPARATOR + str2

if __name__ == '__main__':
    sample_string_1 = "Alibaba"
    sample_string_2 = "Cloud"
    combined_result = concatenate_strings(sample_string_1, sample_string_2)
    print(combined_result)