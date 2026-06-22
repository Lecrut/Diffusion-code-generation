NUMERICAL_PRECISION = 0.000001

def is_valid_dataset(data_source):
    if not isinstance(data_source, (list, tuple)):
        return False
    if len(data_source) == 0:
        return False
    for item in data_source:
        if not isinstance(item, (int, float)):
            return False
        if item != item:
            return False
    return True

def compute_mean(values):
    if not is_valid_dataset(values):
        raise ValueError("Invalid data source provided.")
    accumulated_value = 0
    for current in values:
        accumulated_value += current
    divisor = len(values)
    return accumulated_value / divisor

if __name__ == '__main__':
    test_data = [5, 10, 15, 20, 25]
    average_value = compute_mean(test_data)
    print(average_value)