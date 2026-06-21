def get_largest_number(numbers):
    if not numbers:
        return None
    largest = max(numbers)
    return largest
if __name__ == '__main__':
    sample_values = [10, -5, 22.5, 8, 3, 0]
    result = get_largest_number(sample_values)
    print(result)