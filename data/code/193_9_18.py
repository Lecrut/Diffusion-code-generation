MAX_RETRIES = 3

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

def calculate_total(values):
    try:
        return sum_values(values)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    sample_values = [1, 2, 3.5, 4]
    result = calculate_total(sample_values)
    print(result)