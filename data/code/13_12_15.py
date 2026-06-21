def get_nth_element(s, n):
    try:
        return s[n]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_string = "hello"
    index = -1
    result = get_nth_element(sample_string, index)
    print(result)