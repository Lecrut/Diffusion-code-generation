def find_extremes(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    smallest = largest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    
    return smallest, largest

if __name__ == '__main__':
    sample_values = [7, 3, 9, 1, 5, 12]
    print(find_extremes(sample_values))