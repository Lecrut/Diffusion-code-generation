def find_extremes(numbers):
    if not numbers:
        raise ValueError("Input tuple must not be empty.")
    
    smallest = largest = numbers[0]
    
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    
    return smallest, largest

if __name__ == '__main__':
    sample_values = (15, -3, 88, 0, -42, 99, 1)
    try:
        result = find_extremes(sample_values)
        print(f"Input Tuple: {sample_values}")
        print(f"Smallest value: {result[0]}")
        print(f"Largest value: {result[1]}")
    except ValueError as e:
        print(e)