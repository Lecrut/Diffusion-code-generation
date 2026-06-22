def find_min_max(values):
    return min(values.values()), max(values.values())

if __name__ == '__main__':
    sample_values = {'a': 3, 'b': 5, 'c': 1, 'd': 8}
    print(find_min_max(sample_values))