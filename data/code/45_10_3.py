def find_minimum(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_list)
    print(result)