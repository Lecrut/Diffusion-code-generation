def lexicographic_compare(str1, str2):
    if str1 < str2:
        return -1
    if str1 > str2:
        return 1
    return 0

if __name__ == '__main__':
    string1 = "orange"
    string2 = "grape"
    result = lexicographic_compare(string1, string2)
    print(result)