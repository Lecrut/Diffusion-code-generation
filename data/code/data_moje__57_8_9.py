def fibonacci_up_to_index(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

if __name__ == '__main__':
    result = fibonacci_up_to_index(1000)
    print(result)