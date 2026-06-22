MAX_NUMBER = float('inf')
MIN_NUMBER = float('-inf')

def find_difference(numbers):
    if not numbers:
        raise ValueError("The tuple must contain at least one number.")
    
    max_num = MIN_NUMBER
    min_num = MAX_NUMBER
    
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    
    return max_num - min_num

if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    print(find_difference(sample_values))