def fibonacci_20():
    count = 20
    if count <= 0:
        return []
    if count == 1:
        return [0]

    fibs = [0, 1]
    for i in range(2, count):
        next_val = fibs[-1] + fibs[-2]
        fibs.append(next_val)
    return fibs

if __name__ == '__main__':
    print(fibonacci_20())