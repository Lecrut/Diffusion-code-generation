def find_extremes(data):
    if not data:
        return None
    extremes = {'min': data[0], 'max': data[0]}
    for num in data:
        if num < extremes['min']:
            extremes['min'] = num
        if num > extremes['max']:
            extremes['max'] = num
    return extremes['min'], extremes['max']

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 5]
    min_val, max_val = find_extremes(sample_list)
    print(f"Smallest value: {min_val}")
    print(f"Largest value: {max_val}")