def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fibs = [0] * n
    fibs[0] = 0
    fibs[1] = 1
    
    a = 0
    b = 1
    
    for i in range(2, n):
        a, b = b, a + b
        fibs[i] = b
        
    return fibs

if __name__ == '__main__':
    fib_sequence = generate_fibonacci(100)
    print(fib_sequence)