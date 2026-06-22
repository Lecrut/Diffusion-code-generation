def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib_numbers = [0, 1]
    for _ in range(2, n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers

if __name__ == '__main__':
    result = generate_fibonacci(20)
    print(result)