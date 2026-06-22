def find_second_smallest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    smallest = second_smallest = float('inf')
    
    for number in numbers:
        if number <= smallest:
            smallest, second_smallest = number, smallest
        elif number < second_smallest:
            second_smallest = number
    
    return second_smallest

if __name__ == '__main__':
    sample_list = [4, 2, 9, 7, 5, 1]
    print(find_second_smallest(sample_list))