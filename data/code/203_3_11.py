def lexicographical_compare(str1, str2):
    return str1 < str2

if __name__ == '__main__':
    sample_str1 = "cherry"
    sample_str2 = "banana"
    result = lexicographical_compare(sample_str1, sample_str2)
    print(result)