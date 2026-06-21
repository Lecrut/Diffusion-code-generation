def compare_strings(str1, str2):
    len_diff = len(str1) - len(str2)
    if len_diff != 0:
        return (str1, str2) if len_diff > 0 else (str2, str1)
    
    alpha_diff = ord(str1[0]) - ord(str2[0])
    if alpha_diff != 0:
        return (str1, str2) if alpha_diff < 0 else (str2, str1)
    
    return ('', '')

if __name__ == '__main__':
    print(compare_strings("apple", "banana"))
    print(compare_strings("banana", "apple"))
    print(compare_strings("apple", "apple"))