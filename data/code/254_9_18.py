def second_smallest(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    first, second = float('inf'), float('inf')
    
    for num in numbers:
        if num <= first:
            first, second = num, first
        elif num < second:
            second = num
    
    return second

if __name__ == '__main__':
    sample_list = [4, 2, 9, 7, 5, 1]
    print(second_smallest(sample_list))