def get_nth_element(s, n):
    if not isinstance(s, str):
        raise TypeError("First argument must be a string")
    if not isinstance(n, int):
        raise TypeError("Second argument must be an integer")
    if len(s) == 0:
        return None
    if n >= len(s) or n < -len(s):
        return None
    return s[n]

if __name__ == '__main__':
    sample_string = "hello"
    print(get_nth_element(sample_string, 0))
    print(get_nth_element(sample_string, -1))
    print(get_nth_element(sample_string, 2))
    print(get_nth_element(sample_string, 10))
    print(get_nth_element(sample_string, -10))
    print(get_nth_element("", 0))