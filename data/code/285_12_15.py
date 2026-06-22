MAX_VALUE = "max"

def compare_adjacent_elements(data):
    return tuple(max(a, b) for a, b in zip(data, data[1:]))

if __name__ == '__main__':
    sample_data = (3, 1, 4, 1, 5, 9, 2)
    result = compare_adjacent_elements(sample_data)
    print(result)