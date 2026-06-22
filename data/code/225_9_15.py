def find_min_max(values):
    return min(values.values()), max(values.values())

if __name__ == '__main__':
    sample_values = {
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    }
    print(find_min_max(sample_values))