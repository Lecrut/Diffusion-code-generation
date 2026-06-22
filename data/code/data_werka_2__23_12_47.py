def lexicographic_compare(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    
    return (str1 > str2) - (str1 < str2)

if __name__ == '__main__':
    string1 = "kiwi"
    string2 = "mango"
    result = lexicographic_compare(string1, string2)
    print(result)