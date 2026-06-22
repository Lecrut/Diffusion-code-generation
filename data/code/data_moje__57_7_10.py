def bitwise_fibonacci():
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    fib = [0, 1]
    a = 0
    b = 1
    for _ in range(2, n):
        a, b = b, a + b
        fib.append(b)
    return fib

if __name__ == '__main__':
    terms = bitwise_fibonacci()
    limit = 100
    while len(terms) < limit:
        next_val = terms[-1] + terms[-2]
        terms.append(next_val)
    for i in range(limit):
        print(terms[i])