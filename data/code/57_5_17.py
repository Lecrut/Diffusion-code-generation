import math

def compute_fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    
    fib_n = (phi**n - psi**n) / sqrt_5
    return round(fib_n)

def generate_fibonacci_sequence(count):
    if count <= 0:
        return []
    
    fibs = []
    for i in range(count):
        fibs.append(compute_fibonacci(i))
    return fibs

if __name__ == '__main__':
    first_80 = generate_fibonacci_sequence(80)
    for i, val in enumerate(first_80):
        print(f"F({i}) = {val}")
    
    print(f"F(10) = {compute_fibonacci(10)}")
    print(f"F(20) = {compute_fibonacci(20)}")
    print(f"F(50) = {compute_fibonacci(50)}")
    print(f"F(79) = {compute_fibonacci(79)}")