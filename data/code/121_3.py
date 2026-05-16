def compare_lengths(str1, str2):
    if len(str1) >= len(str2):
        return str1
    else:
        return str2
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result = compare_lengths(string_a, string_b)
    print(result)