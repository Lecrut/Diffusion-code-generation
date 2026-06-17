def compare_string_lengths(str1, str2):
    lengths = tuple(sorted((len(str1), len(str2))))
    return lengths
if __name__ == '__main__':
    s1 = "apple"
    s2 = "banana"
    result = compare_string_lengths(s1, s2)
    print(result)
    s3 = "short"
    s4 = "longerstring"
    result2 = compare_string_lengths(s3, s4)
    print(result2)
    s5 = "test"
    s6 = "testing"
    result3 = compare_string_lengths(s5, s6)
    print(result3)