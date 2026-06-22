def extract_element(t, position):
    if 0 <= position < len(t):
        return t[position]
    return None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(extract_element(sample_tuple, 2))
    print(extract_element(sample_tuple, 5))
    print(extract_element(sample_tuple, -1))
    print(extract_element(sample_tuple, 0))