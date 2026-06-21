FIBONACCI_COUNT = 10

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

if __name__ == '__main__':
    fibonacci_numbers = generate_fibonacci(FIBONACCI_COUNT)
    print(fibonacci_numbers)