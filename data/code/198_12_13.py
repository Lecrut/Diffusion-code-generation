def find_lowest_value(numbers):
    if not numbers:
        return None
    lowest = min(numbers)
    return lowest
if __name__ == '__main__':
    sample_values = [-3, 10, -8, 2, -5]
    result = find_lowest_value(sample_values)
    print(result)