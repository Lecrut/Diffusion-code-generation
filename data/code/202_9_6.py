def find_maximum(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    
    return max_value

if __name__ == '__main__':
    result = find_maximum(3, 5, 1)
    print(result)