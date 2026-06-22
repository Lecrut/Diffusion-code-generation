def fetch_nth_element(s, n):
    if not isinstance(s, str):
        raise TypeError("First argument must be a string")
    length = len(s)
    if n >= -length and n < length:
        return s[n]
    return None

if __name__ == '__main__':
    test_string = "Python"
    print(fetch_nth_element(test_string, 1))
    print(fetch_nth_element(test_string, -1))
    print(fetch_nth_element(test_string, 10))