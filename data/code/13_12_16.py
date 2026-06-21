def get_nth_element(s: str, n: int) -> str:
    length = len(s)
    if n < 0:
        n = n + length
    if 0 <= n < length:
        return s[n]
    return ""

if __name__ == '__main__':
    sample_string = "hello"
    print(get_nth_element(sample_string, 1))
    print(get_nth_element(sample_string, -2))
    print(get_nth_element(sample_string, 10))