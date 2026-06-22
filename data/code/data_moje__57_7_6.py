def fibonacci_bitwise(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    if count == 2:
        return [0, 1]
    fibs = [0, 1]
    a, b = 0, 1
    for _ in range(2, count):
        c = a | b
        if a & b:
            c = (c << 1) - a - b
        a = b
        b = c
        fibs.append(c)
    return fibs

if __name__ == '__main__':
    result = fibonacci_bitwise(100)
    for term in result:
        print(term)