def sum_sequence(numbers):
    if not all((isinstance(n, int) for n in numbers)):
        raise ValueError('All elements in the sequence must be integers.')
    return sum(numbers)
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    try:
        result = sum_sequence(sample_numbers)
        print(result)
    except ValueError as e:
        print(e)