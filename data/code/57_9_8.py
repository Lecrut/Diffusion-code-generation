def get_fibonacci_first_75():
    result = []
    a = 0
    b = 1
    for _ in range(75):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    numbers = get_fibonacci_first_75()
    print(numbers)