def extract_element(t, pos):
    try:
        return t[pos]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(extract_element(sample_tuple, 2))
    print(extract_element(sample_tuple, 10))
    print(extract_element(sample_tuple, 0))
    print(extract_element(sample_tuple, -1))