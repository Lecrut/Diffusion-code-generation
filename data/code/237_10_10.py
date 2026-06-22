MAX_TERMS = 20

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    sequence = fibonacci(MAX_TERMS)
    print(sequence)