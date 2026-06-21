def find_maximum(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    return max(a, b, c)

if __name__ == '__main__':
    result1 = find_maximum(10, 20, 30)
    print(f"Maximum of (10, 20, 30): {result1}")