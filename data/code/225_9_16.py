def extract_min_max(data):
    return min(data.values()), max(data.values())

if __name__ == '__main__':
    sample_data = {'a': 3, 'b': 5, 'c': 1, 'd': 8}
    print(extract_min_max(sample_data))