def calculate_range(data):
    values = list(data.values())
    if not values:
        return None
    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val
    return range_val, [label for label, value in data.items() if value == min_val or value == max_val]

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 10
    }
    result = calculate_range(sample_data)
    print(result)