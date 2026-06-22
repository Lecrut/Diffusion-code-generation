def sum_sequence(numbers):
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers.")
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = sum_sequence(sample_numbers)
    print(result)