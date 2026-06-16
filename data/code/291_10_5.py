def compare_string_lengths(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 > length2:
        return f"String 1 ({len(str1)}) is longer than String 2 ({len(str2)})."
    elif length2 > length1:
        return f"String 2 ({len(str2)}) is longer than String 1 ({len(str1)})."
    else:
        return f"String 1 and String 2 have the same length: {len(str1)}."
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result = compare_string_lengths(string_a, string_b)
    print(result)