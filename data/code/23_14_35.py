def lexicographic_compare(str1, str2):
    return (str1 > str2) - (str1 < str2)

if __name__ == '__main__':
    STRING_ONE = "grape"
    STRING_TWO = "orange"
    result = lexicographic_compare(STRING_ONE, STRING_TWO)
    print(result)