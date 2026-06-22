import math

def find_max_element():
    numbers = [3.14, 2.71, 1.618, 0.577, 9.806, 1.414, 2.236]
    
    if not numbers:
        return None
        
    max_val = numbers[0]
    
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
            
    return max_val

if __name__ == '__main__':
    result = find_max_element()
    print(result)