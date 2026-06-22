def max_min_difference(data):
    return max(data.values()) - min(data.values())

if __name__ == '__main__':
    sample_data = {'a': 3, 'b': 5, 'c': 1, 'd': 8}
    print(max_min_difference(sample_data))