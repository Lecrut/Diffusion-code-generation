def lexicographic_compare(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    comparison_map = {
        -1: "str1 < str2",
        0: "str1 == str2",
        1: "str1 > str2"
    }
    
    result = (str1 > str2) - (str1 < str2)
    return result

if __name__ == '__main__':
    string1 = "mango"
    string2 = "kiwi"
    result = lexicographic_compare(string1, string2)
    print(result)