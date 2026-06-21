def lexicographic_compare(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    comparison_table = {
        -1: "First string is less than the second",
        0: "Strings are equal",
        1: "First string is greater than the second"
    }
    
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    string1 = "kiwi"
    string2 = "mango"
    result = lexicographic_compare(string1, string2)
    print(result)