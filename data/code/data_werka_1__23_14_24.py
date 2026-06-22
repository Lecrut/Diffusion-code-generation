def compare_strings(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    string_a = "apple"
    string_b = "banana"
    result = compare_strings(string_a, string_b)
    print(result)