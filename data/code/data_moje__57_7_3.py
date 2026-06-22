import sys

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def get_fibonacci_terms(count):
    if count <= 0:
        return []
    
    terms = []
    a, b = 0, 1
    
    for _ in range(count):
        terms.append(a)
        a, b = b, a + b
    
    return terms

if __name__ == '__main__':
    count = 100
    result = get_fibonacci_terms(count)
    for i, val in enumerate(result):
        print(f"F({i}) = {val}")