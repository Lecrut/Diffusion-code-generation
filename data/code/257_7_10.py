def max_min_difference(data):
    return max(data.values()) - min(data.values())

if __name__ == '__main__':
    sample_data = {'a': 5, 'b': 3, 'c': 9, 'd': 1}
    print(max_min_difference(sample_data))