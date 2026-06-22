def get_nth_element(s: str, n: int) -> str:
    length = len(s)
    if length == 0:
        return None
    if n < 0:
        n = length + n
    if n < 0 or n >= length:
        return None
    return s[n]

if __name__ == '__main__':
    sample_string = "HelloWorld"
    index1 = 3
    index2 = -2
    index3 = 15
    print(get_nth_element(sample_string, index1))
    print(get_nth_element(sample_string, index2))
    print(get_nth_element(sample_string, index3))