def get_middle_value(values):
    if not values:
        raise ValueError("List cannot be empty")
    sorted_values = sorted(values)
    mid_index = len(sorted_values) // 2
    if len(sorted_values) % 2 == 0:
        return (sorted_values[mid_index - 1] + sorted_values[mid_index]) / 2
    return sorted_values[mid_index]

if __name__ == '__main__':
    sample_array = [7, 3, 1, 9, 5]
    result = get_middle_value(sample_array)
    print(result)