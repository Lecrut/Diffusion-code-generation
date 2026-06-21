def lexicographic_compare(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    string1 = "pear"
    string2 = "peach"
    result = lexicographic_compare(string1, string2)
    print(result)