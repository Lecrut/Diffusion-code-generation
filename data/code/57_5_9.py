import math

def fibonacci_sequence(n):
    results = []
    for i in range(n):
        phi = (1 + math.sqrt(5)) / 2
        psi = (1 - math.sqrt(5)) / 2
        fib = (phi ** i - psi ** i) / math.sqrt(5)
        results.append(round(fib))
    return results

if __name__ == '__main__':
    print(fibonacci_sequence(80))