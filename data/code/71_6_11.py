def get_lower_median(values):
    if not values:
        raise ValueError("Cannot compute median of an empty sequence")
    sorted_values = sorted(values)
    count = len(sorted_values)
    lower_index = (count - 1) // 2
    return sorted_values[lower_index]

if __name__ == '__main__':
    sample_data = [9, 3, 7, 1, 5]
    result = get_lower_median(sample_data)
    print(result)