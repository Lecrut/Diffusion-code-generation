def average_values(d):
    values = [v for v in d.values() if isinstance(v, (int, float))]
    if not values:
        raise ValueError("No valid numbers found")
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 'text', 'd': 30}
    try:
        print(average_values(sample_dict))
    except ValueError as e:
        print(e)