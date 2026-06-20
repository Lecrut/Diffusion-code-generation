def filter_numbers(numbers, divisible_by=None, parity=None):
    result = []
    for number in numbers:
        if (divisible_by is None or number % divisible_by == 0) and (parity is None or (parity == 'even' and number % 2 == 0) or (parity == 'odd' and number % 2 != 0)):
            result.append(number)
    return result
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_numbers(sample_numbers, divisible_by=2))
    print(filter_numbers(sample_numbers, parity='odd'))
    print(filter_numbers(sample_numbers, divisible_by=3, parity='even'))