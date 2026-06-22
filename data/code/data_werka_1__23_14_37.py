def compare_lexicographically(str1, str2):
    if str1 < str2:
        return -1
    if str1 > str2:
        return 1
    return 0

if __name__ == '__main__':
    string1 = "orange"
    string2 = "mango"
    result = compare_lexicographically(string1, string2)
    print(result)