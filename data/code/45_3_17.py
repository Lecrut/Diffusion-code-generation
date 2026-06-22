def min_value(numbers):
    if not numbers:
        return None
    return min(numbers)

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = min_value(sample_numbers)
    print(result)