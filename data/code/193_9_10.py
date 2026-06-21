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

def safe_sum(values):
    try:
        return sum_values(values)
    except (TypeError, ValueError) as e:
        print(e)
        return None

if __name__ == '__main__':
    sample_values = [15, 25.75, "35", 45]
    result = safe_sum(sample_values)
    if result is not None:
        print(result)