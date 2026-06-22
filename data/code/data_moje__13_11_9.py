def extract_at_position(t, pos):
    if pos < 0 or pos >= len(t):
        return None
    return t[pos]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(extract_at_position(sample_tuple, 0))
    print(extract_at_position(sample_tuple, 2))
    print(extract_at_position(sample_tuple, 4))
    print(extract_at_position(sample_tuple, 5))
    print(extract_at_position(sample_tuple, -1))