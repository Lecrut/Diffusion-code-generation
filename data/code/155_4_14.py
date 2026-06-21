def sum_numbers(numbers):
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of numbers")
    return sum(numbers)

if __name__ == '__main__':
    sample1 = [7, 8, 9]
    sample2 = []
    print(sum_numbers(sample1))
    try:
        print(sum_numbers('not a list'))
    except ValueError as e:
        print(e)