def get_fibonacci_75():
    fibs = [0, 1]
    for _ in range(73):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

if __name__ == '__main__':
    result = get_fibonacci_75()
    print(result)