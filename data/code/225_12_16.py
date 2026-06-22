def find_min_max(values):
    if not values:
        return (None, None)
    min_value = min(values.values(), key=lambda x: (x, -values[x]))
    max_value = max(values.values(), key=lambda x: (-x, values[x]))
    min_key = next((key for key, value in values.items() if value == min_value))
    max_key = next((key for key, value in values.items() if value == max_value))
    return ((min_key, min_value), (max_key, max_value))
if __name__ == '__main__':
    sample_values = {'a': 3, 'b': 5, 'c': 1, 'd': 8}
    result = find_min_max(sample_values)
    print(result)