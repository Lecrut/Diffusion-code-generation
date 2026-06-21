def extract_element(t, position):
    if position < 0 or position >= len(t):
        return None
    return t[position]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(extract_element(sample_tuple, 2))
    print(extract_element(sample_tuple, 5))
    print(extract_element(sample_tuple, -1))
    print(extract_element(sample_tuple, 0))