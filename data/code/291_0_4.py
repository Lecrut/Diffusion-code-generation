def compare_string_lengths(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 > length2:
        return f"String 1 ('{str1}') is longer than String 2 ('{str2}'). Lengths: {length1} vs {length2}"
    elif length2 > length1:
        return f"String 2 ('{str2}') is longer than String 1 ('{str1}'). Lengths: {length2} vs {length1}"
    else:
        return f"String 1 ('{str1}') and String 2 ('{str2}') have the same length. Lengths: {length1} vs {length2}"
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result = compare_string_lengths(string_a, string_b)
    print(result)
    string_c = "python"
    string_d = "programming"
    result2 = compare_string_lengths(string_c, string_d)
    print(result2)
    string_e = "test"
    string_f = "test"
    result3 = compare_string_lengths(string_e, string_f)
    print(result3)