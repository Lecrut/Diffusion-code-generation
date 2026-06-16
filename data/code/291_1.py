def compare_string_lengths(str1, str2):
    lengths = tuple(sorted((len(str1), len(str2))))
    return lengths
if __name__ == '__main__':
    s1 = "apple"
    s2 = "banana"
    result = compare_string_lengths(s1, s2)
    print(result)