def filter_integers(numbers, divisible_by=None, is_even=None):
    if not all((isinstance(n, int) for n in numbers)):
        raise ValueError('All elements in the list must be integers.')
    filtered_numbers = []
    for number in numbers:
        if (divisible_by is None or number % divisible_by == 0) and (is_even is None or (number % 2 == 0) == is_even):
            filtered_numbers.append(number)
    return filtered_numbers
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results1 = filter_integers(sample_numbers, divisible_by=2)
    print(results1)
    results2 = filter_integers(sample_numbers, is_even=True)
    print(results2)
    results3 = filter_integers(sample_numbers, divisible_by=3, is_even=False)
    print(results3)