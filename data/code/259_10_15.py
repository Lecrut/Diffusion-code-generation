def find_extremes(numbers):
    if not numbers:
        return None
    smallest = min(numbers)
    largest = max(numbers)
    return (smallest, largest)
if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_extremes(sample_values)
    print(result)