def compute_factorial(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    result = 1
    current = n
    while current > 1:
        result *= current
        current -= 1
    return result

if __name__ == '__main__':
    sample_values = [0, 1, 5, 10, 20]
    
    for val in sample_values:
        result = compute_factorial(val)
        print(f"{val}! = {result}")