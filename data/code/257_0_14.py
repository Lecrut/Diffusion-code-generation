MAX_VALUE = float('inf')
MIN_VALUE = float('-inf')

def calculate_difference(numbers):
    max_val = MIN_VALUE
    min_val = MAX_VALUE
    
    for num in numbers:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
            
    return max_val - min_val

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    result = calculate_difference(sample_values)
    print(result)