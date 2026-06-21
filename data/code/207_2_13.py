def find_max_in_tuple(floats):
    if not floats:
        raise ValueError("Input tuple cannot be empty")
    return max(floats)

if __name__ == '__main__':
    sample_values = (3.5, 2.1, 4.8, 1.9)
    print(find_max_in_tuple(sample_values))