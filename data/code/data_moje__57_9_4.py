def fibonacci_first_75():
    count = 75
    fibs = [0] * count
    fibs[0] = 0
    if count > 1:
        fibs[1] = 1
        for i in range(2, count):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs

if __name__ == '__main__':
    result = fibonacci_first_75()
    print(result)