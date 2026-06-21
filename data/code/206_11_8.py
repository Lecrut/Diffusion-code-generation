def find_min_element(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")
    min_element = numbers[0]
    for number in numbers:
        if number < min_element:
            min_element = number
    return min_element

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    print(find_min_element(sample_values))