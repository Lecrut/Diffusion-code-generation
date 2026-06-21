def find_second_smallest_largest(numbers):
    if len(numbers) < 2:
        return None, None
    
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
        
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    
    return second_smallest if second_smallest != float('inf') else None, second_largest if second_largest != float('-inf') else None

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 1, 5, 6]
    print(find_second_smallest_largest(sample_numbers))