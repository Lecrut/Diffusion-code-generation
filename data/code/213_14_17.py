FIBONACCI_COUNT = 10

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    result = [0, 1]
    for _ in range(2, n):
        next_value = result[-1] + result[-2]
        result.append(next_value)
    return result

if __name__ == '__main__':
    fibonacci_sequence = generate_fibonacci(FIBONACCI_COUNT)
    print(fibonacci_sequence)