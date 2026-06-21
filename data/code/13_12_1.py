def fetch_nth_element(s, n):
    if not s:
        return None
    length = len(s)
    if n >= -length and n < length:
        return s[n]
    return None

if __name__ == '__main__':
    sample_string = "HelloWorld"
    print(fetch_nth_element(sample_string, 0))
    print(fetch_nth_element(sample_string, -1))
    print(fetch_nth_element(sample_string, 5))
    print(fetch_nth_element(sample_string, -100))
    print(fetch_nth_element(sample_string, 100))