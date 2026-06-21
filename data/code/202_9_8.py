def find_maximum(a, b, c):
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("All inputs must be integers")
    
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    
    return max_value

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    sample_c = 15
    
    result = find_maximum(sample_a, sample_b, sample_c)
    print(result)