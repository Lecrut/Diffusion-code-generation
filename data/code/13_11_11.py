def extract_element(tup, position):
    try:
        return tup[position]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(extract_element(sample_tuple, 2))
    print(extract_element(sample_tuple, 10))
    print(extract_element(sample_tuple, 0))
    print(extract_element(sample_tuple, 4))