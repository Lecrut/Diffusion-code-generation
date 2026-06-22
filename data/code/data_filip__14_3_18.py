def check_unique_chars(s):
    if s is None:
        return False
    chars = list(s)
    n = len(chars)
    for i in range(n):
        for j in range(i + 1, n):
            if chars[i] == chars[j]:
                return False
    return True

if __name__ == '__main__':
    sample_string = "abcde"
    result = check_unique_chars(sample_string)
    print(result)
    sample_string_duplicate = "abca"
    result_duplicate = check_unique_chars(sample_string_duplicate)
    print(result_duplicate)