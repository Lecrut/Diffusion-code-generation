def sum_values(values):
    if not hasattr(values, '__iter__'):
        raise TypeError("Input is not iterable")
    total = 0
    for value in values:
        if isinstance(value, (int, float)):
            total += value
        else:
            raise ValueError(f"Non-numeric value encountered: {value}")
    return total

def calculate_sum(data):
    try:
        result = sum_values(data)
        return result
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    sample_data = [15, 25.7, 30, "40"]
    result = calculate_sum(sample_data)
    print(result)