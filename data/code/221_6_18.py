def order_three(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers.")
    
    min_val = min(a, b, c)
    max_val = max(a, b, c)
    middle_val = a + b + c - min_val - max_val
    return (min_val, middle_val, max_val)

if __name__ == '__main__':
    x = 5
    y = 2
    z = 8
    result = order_three(x, y, z)
    print(result)