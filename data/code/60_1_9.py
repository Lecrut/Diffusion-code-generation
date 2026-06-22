def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    result = 1
    current = n
    
    while current > 0:
        result *= current
        current -= 1
    
    return result

if __name__ == '__main__':
    test_values = [0, 1, 5, 7, 10]
    
    for val in test_values:
        result = factorial(val)
        print(f"{val}! = {result}")