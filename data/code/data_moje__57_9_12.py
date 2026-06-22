def fibonacci_first_75():
    count = 75
    result = [0] * count
    if count >= 1:
        result[0] = 0
    if count >= 2:
        result[1] = 1
    for i in range(2, count):
        result[i] = result[i - 1] + result[i - 2]
    return result

if __name__ == '__main__':
    print(fibonacci_first_75())