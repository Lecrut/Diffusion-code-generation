def compare_strings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        difference = len1 - len2
        longer_string = str1
        shorter_string = str2
    elif len2 > len1:
        difference = len2 - len1
        longer_string = str2
        shorter_string = str1
    else:
        difference = 0
        longer_string = str1
        shorter_string = str2
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")
    print(f"{longer_string} has more characters than {shorter_string} by {difference}.")
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    compare_strings(string_a, string_b)
    string_c = "programming"
    string_d = "python"
    compare_strings(string_c, string_d)
    string_e = "short"
    string_f = "longerstring"
    compare_strings(string_e, string_f)