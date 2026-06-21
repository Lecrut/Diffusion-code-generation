MIN_VALUE = float('-inf')

def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    smallest = MIN_VALUE
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 4]
    result = find_smallest(sample_values)
    print(result)