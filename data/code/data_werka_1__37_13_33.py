JOIN_DELIMITER = " and "

def merge_strings(str1, str2):
    return str1 + JOIN_DELIMITER + str2

if __name__ == '__main__':
    sample_string_a = "Hello"
    sample_string_b = "World"
    merged_result = merge_strings(sample_string_a, sample_string_b)
    print(merged_result)