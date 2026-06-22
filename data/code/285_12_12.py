def max_adjacent_elements(data):
    return tuple(max(a, b) for a, b in zip(data, data[1:]))

if __name__ == '__main__':
    sample_data = (3, 5, 2, 8, 4)
    print(max_adjacent_elements(sample_data))