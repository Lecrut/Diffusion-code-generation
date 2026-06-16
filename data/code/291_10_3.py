def compare_string_lengths(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 > length2:
        return f"{str1} is longer than {str2}"
    elif length2 > length1:
        return f"{str2} is longer than {str1}"
    else:
        return f"{str1} and {str2} have the same length"
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result = compare_string_lengths(string_a, string_b)
    print(result)