def extract_element_at_position(t, position):
    if position < 0 or position >= len(t):
        return None
    return t[position]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(extract_element_at_position(sample_tuple, 2))
    print(extract_element_at_position(sample_tuple, 5))
    print(extract_element_at_position(sample_tuple, -1))
    print(extract_element_at_position(sample_tuple, 0))