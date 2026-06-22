def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0] * n
    fib[0] = 0
    fib[1] = 1
    
    i = 2
    while i < n:
        fib[i] = fib[i - 1] + fib[i - 2]
        i += 1
    
    return fib

if __name__ == '__main__':
    terms = generate_fibonacci(100)
    for term in terms:
        print(term)