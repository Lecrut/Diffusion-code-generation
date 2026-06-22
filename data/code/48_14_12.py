def find_max_custom(array):
    if not array:
        raise ValueError("Array must not be empty")
    
    max_val = array[0]
    max_idx = 0
    n = len(array)
    i = 1
    while i < n:
        val = array[i]
        if val > max_val or (val == max_val and i > max_idx):
            max_val = val
            max_idx = i
        i += 1
    
    return max_val

if __name__ == '__main__':
    numbers = [3.14, 1.41, 2.72, 0.58, 9.99, 1.23, 7.89]
    result = find_max_custom(numbers)
    print(result)