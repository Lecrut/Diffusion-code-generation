def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    print(find_smallest(sample_values))