def find_maximum(a, b, c):
    if not all(isinstance(x, int) for x in [a, b, c]):
        raise ValueError("All inputs must be integers")
    
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    
    return max_value

if __name__ == '__main__':
    sample_max = find_maximum(34, 78, 56)
    print(sample_max)