def find_largest_integer(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers")
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [100, 200, 50, 300, 75]
    try:
        result = find_largest_integer(sample_values)
        print(result)
    except ValueError as e:
        print(e)