def find_max_pairs(data):
    return [max(a, b) for a, b in zip(data, data[1:])]

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_max_pairs(sample_values)
    print(result)