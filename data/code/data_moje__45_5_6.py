def find_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not numbers:
        raise ValueError("List cannot be empty")
    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum

if __name__ == '__main__':
    sample_data = [34, 12, 56, 1, 99, 4]
    result = find_minimum(sample_data)
    print(result)
    try:
        find_minimum("not a list")
    except TypeError as e:
        print(e)