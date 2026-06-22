def fibonacci_75():
    result = [0, 1]
    a, b = 0, 1
    for _ in range(73):
        a, b = b, a + b
        result.append(b)
    return result[:75]

if __name__ == '__main__':
    print(fibonacci_75())