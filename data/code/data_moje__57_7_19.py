def fibonacci_first_100():
    count = 100
    if count <= 0:
        return []
    if count == 1:
        return [0]
    
    fib_sequence = [0] * count
    fib_sequence[0] = 0
    fib_sequence[1] = 1
    
    for i in range(2, count):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]
    
    return fib_sequence

if __name__ == '__main__':
    result = fibonacci_first_100()
    print(result)