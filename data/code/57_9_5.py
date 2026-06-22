def fibonacci_75():
    a, b = 0, 1
    result = []
    for _ in range(75):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    print(fibonacci_75())