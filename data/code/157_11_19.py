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
        [3, 1, 4, 1, 5, 9, 2],
        [-10, 5, 0, -3, 12],
        [42],
        [7],
        []
    ]
    
    for i, lst in enumerate(sample_lists):
        try:
            print(f"Smallest in list {i+1}: {find_smallest(lst)}")
        except ValueError as e:
            print(e)