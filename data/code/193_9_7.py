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

def main():
    sample_values = [15, 25.75, 35, "45"]
    try:
        result = sum_values(sample_values)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)

if __name__ == '__main__':
    main()