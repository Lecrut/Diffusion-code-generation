def find_min_max(numbers):
    if not numbers:
        raise ValueError("The input tuple must contain at least one element.")
    
    minimum = float('inf')
    maximum = float('-inf')
    
    for number in numbers:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    
    return (minimum, maximum)

if __name__ == '__main__':
    sample_tuple = (10, 4, 25, 8, 30, 15)
    min_max_result = find_min_max(sample_tuple)
    print(min_max_result)