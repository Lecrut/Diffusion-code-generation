def fibonacci_200():
    a, b = 0, 1
    result = []
    for _ in range(200):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    print(fibonacci_200())