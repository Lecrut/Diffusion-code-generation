def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, 0.577, -1.0]
    result = find_smallest(sample_list)
    print(result)