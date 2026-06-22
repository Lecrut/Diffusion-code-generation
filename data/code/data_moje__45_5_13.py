def find_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("List must not be empty")
    minimum = numbers[0]
    for num in numbers[1:]:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")
        if num < minimum:
            minimum = num
    return minimum

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 67, 90]
    result = find_minimum(sample_list)
    print(result)