def generate_fibonacci(n):
    return [next_fib if (next_fib := a + b) else a for a, b in ([(0, 1) if i == 0 else (b, a + b) for i, (a, b) in enumerate([(0, 1)] * n)] for i in range(n))][0:n]

def get_fibonacci_sequence(count):
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    fibs = [0, 1]
    for _ in range(2, count):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

if __name__ == '__main__':
    print(get_fibonacci_sequence(15))