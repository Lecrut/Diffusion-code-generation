def get_nth_char(s, n):
    if not s:
        return None
    if n < 0:
        n = len(s) + n
    if 0 <= n < len(s):
        return s[n]
    return None

if __name__ == '__main__':
    sample_string = "HelloWorld"
    index_positive = 3
    index_negative = -2
    index_out_of_bounds = 15
    result1 = get_nth_char(sample_string, index_positive)
    result2 = get_nth_char(sample_string, index_negative)
    result3 = get_nth_char(sample_string, index_out_of_bounds)
    print(result1)
    print(result2)
    print(result3)