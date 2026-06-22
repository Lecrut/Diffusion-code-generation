def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    try:
        print(fibonacci(20))
    except ValueError as e:
        print(e)