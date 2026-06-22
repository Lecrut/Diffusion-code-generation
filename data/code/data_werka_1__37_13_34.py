def merge_strings(str1, str2):
    delimiter = " | "
    return str1 + delimiter + str2

if __name__ == '__main__':
    sample_string_1 = "Python"
    sample_string_2 = "Programming"
    merged_result = merge_strings(sample_string_1, sample_string_2)
    print(merged_result)