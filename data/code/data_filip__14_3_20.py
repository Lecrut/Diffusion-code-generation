def is_unique_chars(s):
    if s is None:
        return False
    char_list = list(s)
    char_list.sort()
    n = len(char_list)
    if n == 0:
        return True
    for i in range(1, n):
        if char_list[i] == char_list[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_1 = "abcdef"
    sample_2 = "aabbcc"
    result_1 = is_unique_chars(sample_1)
    result_2 = is_unique_chars(sample_2)
    print(result_1)
    print(result_2)