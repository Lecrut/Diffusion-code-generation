def fibonacci_bitwise(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fibs = [0, 1]
    a, b = (0, 1)
    count = 2
    while count < n:
        c = a + b
        fibs.append(c)
        a = b
        b = c
        count += 1
    return fibs

def main():
    n = 100
    result = fibonacci_bitwise(n)
    for term in result:
        print(term)
if __name__ == '__main__':
    main()