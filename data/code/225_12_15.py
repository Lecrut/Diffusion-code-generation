def find_min_max(d):
    min_val = min(d.items(), key=lambda x: x[1])
    max_val = max(d.items(), key=lambda x: x[1])
    return (min_val, max_val)

if __name__ == '__main__':
    sample_dict = {'a': 3, 'b': 1, 'c': 2}
    result = find_min_max(sample_dict)
    print(result)