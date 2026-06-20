def filter_numbers(numbers, criteria):
    return [num for num in numbers if all((criterion(num) for criterion in criteria))]
if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 68, 90]
    criteria = [lambda x: x % 2 == 0, lambda x: x % 3 != 0]
    filtered_numbers = filter_numbers(sample_numbers, criteria)
    print(filtered_numbers)