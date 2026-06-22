def fibonacci(n):
    a = 0
    b = 1
    result = []
    i = 0
    while i < n:
        result.append(a)
        a = b
        b = a + b
        i += 1
    return result

def fibonacci_bitwise(n):
    result = []
    a = 0
    b = 1
    count = 0
    while count < n:
        result.append(a)
        temp_a = a
        a = b
        b = temp_a + b
        count += 1
    return result

if __name__ == '__main__':
    terms = 100
    fib_terms = fibonacci_bitwise(terms)
    print(fib_terms)