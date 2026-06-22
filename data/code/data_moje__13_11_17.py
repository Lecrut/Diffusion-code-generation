def extract_at_position(tup, position):
    try:
        return tup[position]
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(extract_at_position(sample_tuple, 0))
    print(extract_at_position(sample_tuple, 4))
    print(extract_at_position(sample_tuple, 5))
    print(extract_at_position(sample_tuple, -1))
    print(extract_at_position(sample_tuple, -6))
    print(extract_at_position((), 0))
    print(extract_at_position((42,), 0))
    print(extract_at_position((42,), 1))