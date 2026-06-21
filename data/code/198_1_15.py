def find_smallest(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    
    return smallest

if __name__ == '__main__':
    sample_lists = [
        [5, 2, 8, 1, 9],
        [-10, 0, -5, 3],
        [42],
        [7],
        []
    ]
    
    for i, list in enumerate(sample_lists):
        try:
            print(f"The smallest element in {list} is: {find_smallest(list)}")
        except ValueError as e:
            print(f"Error for list {i+1}: {e}")