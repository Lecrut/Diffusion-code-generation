def filter_numbers(numbers, criteria):
    result = []
    for number in numbers:
        if all(criterion(number) for criterion in criteria):
            result.append(number)
    return result

if __name__ == '__main__':
    sample_numbers = [10, 23, 45, 68, 79]
    criteria = [
        lambda x: x % 2 == 0,
        lambda x: x > 50
    ]
    filtered_numbers = filter_numbers(sample_numbers, criteria)
    print(filtered_numbers)