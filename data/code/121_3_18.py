def compare_strings(str1, str2):
    return (str1 > str2) - (str1 < str2)

if __name__ == '__main__':
    print(compare_strings("apple", "banana"))
    print(compare_strings("cherry", "cherry"))
    print(compare_strings("date", "apple"))