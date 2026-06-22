import math

def compute_fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return round((phi ** n - psi ** n) / math.sqrt(5))

if __name__ == '__main__':
    results = []
    for i in range(80):
        val = compute_fibonacci(i)
        results.append(val)
    print(results[:10])
    print(results[-1])