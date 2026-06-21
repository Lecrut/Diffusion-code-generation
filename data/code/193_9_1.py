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

if __name__ == '__main__':
    sample_values = [1, 2, 3.5, 4]
    print(sum_values(sample_values))