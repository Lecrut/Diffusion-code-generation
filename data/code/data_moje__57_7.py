def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fibs = [0, 1]
    for i in range(2, n):
        next_val = fibs[i-1] + fibs[i-2]
        fibs.append(next_val)
    return fibs

if __name__ == '__main__':
    terms = fibonacci(100)
    for term in terms:
        print(term)