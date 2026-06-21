def extract_element(t, pos):
    if 0 <= pos < len(t):
        return t[pos]
    return None

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(extract_element(sample_tuple, 2))
    print(extract_element(sample_tuple, 10))
    print(extract_element(sample_tuple, 0))
    print(extract_element(sample_tuple, -1))
    print(extract_element((), 0))