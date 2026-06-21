def calculate_average(numbers):
    if not isinstance(numbers, list):
        raise ValueError('Input must be a list')
    if not numbers:
        raise ValueError('List cannot be empty')
    try:
        total = sum(numbers)
        count = len(numbers)
        return total / count
    except TypeError as e:
        raise TypeError('All elements in the list must be numeric') from e
if __name__ == '__main__':
    sample_values = [[1, 2, 3, 4, 5], [], ['a', 'b', 'c'], [10, 20, 'error']]
    for values in sample_values:
        try:
            avg = calculate_average(values)
            print(f'Average of {values}: {avg}')
        except Exception as e:
            print(f'Error: {e}')