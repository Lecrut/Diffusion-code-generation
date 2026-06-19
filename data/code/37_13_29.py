def merge_strings(str1, str2):
    SEPARATOR = " and "
    return str1 + SEPARATOR + str2

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    merged_string = merge_strings(string_a, string_b)
    print(merged_string)