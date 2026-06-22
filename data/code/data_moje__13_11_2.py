def extract_element(t, pos):
    if pos < 0 or pos >= len(t):
        return None
    return t[pos]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(extract_element(sample_tuple, 2))
    print(extract_element(sample_tuple, 10))
    print(extract_element(sample_tuple, -1))
    print(extract_element(sample_tuple, 0))