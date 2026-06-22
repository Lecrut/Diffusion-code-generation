def compare_string_lengths(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        return str1
    elif len1 < len2:
        return str2
    else:
        return 'Equal'
if __name__ == '__main__':
    result = compare_string_lengths('hello', 'world')
    print(result)
    result = compare_string_lengths('short', 'longerstring')
    print(result)
    result = compare_string_lengths('same', 'size')
    print(result)