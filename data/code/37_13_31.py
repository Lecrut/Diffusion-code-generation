def merge_strings(str1, str2):
    if not str1 or not str2:
        return ""
    return f"{str1}{str2}"

if __name__ == '__main__':
    string_a = "Hello"
    string_b = "World"
    merged_string = merge_strings(string_a, string_b)
    print(merged_string)