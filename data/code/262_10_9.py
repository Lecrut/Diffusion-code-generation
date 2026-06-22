MIN_VALUE = float('-inf')
MAX_VALUE = float('inf')

def find_min_max(numbers):
    if not numbers:
        return None, None
    
    current_min = MIN_VALUE
    current_max = MAX_VALUE
    
    for number in numbers:
        if number < current_min:
            current_min = number
        elif number > current_max:
            current_max = number
    
    return current_min, current_max

if __name__ == '__main__':
    sample_values = [34, 78, 12, 56, 90, 23]
    print(find_min_max(sample_values))