import math

def fibonacci_closed_form(n):
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    result = (phi**n - psi**n) / sqrt5
    return int(round(result))

if __name__ == '__main__':
    results = []
    for i in range(1, 81):
        results.append(fibonacci_closed_form(i))
    print(results)