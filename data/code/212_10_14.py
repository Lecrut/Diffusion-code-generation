INITIAL_VALUE = float('inf')

def find_min_max(numbers):
    minimum = INITIAL_VALUE
    maximum = -INITIAL_VALUE
    
    for num in numbers:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
            
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")