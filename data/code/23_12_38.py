def lexicographic_compare(str1, str2):
    comparison = (str1 > str2) - (str1 < str2)
    return comparison

if __name__ == '__main__':
    string1 = "cherry"
    string2 = "banana"
    result = lexicographic_compare(string1, string2)
    print(result)