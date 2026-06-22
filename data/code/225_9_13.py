def extract_min_max(values):
    return min(values.values()), max(values.values())

if __name__ == '__main__':
    sample_values = {
        'a': 3,
        'b': 1,
        'c': 4,
        'd': 2
    }
    print(extract_min_max(sample_values))