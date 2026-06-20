def average_dict_values(d):
    numeric_values = [v for v in d.values() if isinstance(v, (int, float))]
    if not numeric_values:
        raise ValueError("No valid numbers found")
    return sum(numeric_values) / len(numeric_values)

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20.5, 'c': 'text', 'd': 30}
    print(average_dict_values(sample_dict))