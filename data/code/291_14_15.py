def compare_string_lengths(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        return "String 1 is longer"
    elif len1 < len2:
        return "String 2 is longer"
    else:
        return "Strings are equal in length"

if __name__ == '__main__':
    string1 = "Hello, World!"
    string2 = "Goodbye, World!"
    result = compare_string_lengths(string1, string2)
    print(result)