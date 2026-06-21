def find_min_max(numbers):
    if not numbers:
        return None
    minimum = min(numbers)
    maximum = max(numbers)
    return (minimum, maximum)

if __name__ == '__main__':
    sample_values = [10, 4, 25, 8, 30, 15]
    result = find_min_max(sample_values)
    print(result)