def get_fibonacci_75():
    if 75 < 1:
        return []
    if 75 == 1:
        return [0]
    fibs = [0, 1]
    for _ in range(2, 75):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
if __name__ == '__main__':
    result = get_fibonacci_75()
    print(result)