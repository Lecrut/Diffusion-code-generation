def compare_lexicographically(str1, str2):
    return (str1 > str2) - (str1 < str2)

if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    result = compare_lexicographically(string_a, string_b)
    print(result)