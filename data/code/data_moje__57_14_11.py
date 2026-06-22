def fibonacci_generator(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    values = [0, 1]
    for _ in range(count - 2):
        values.append(values[-1] + values[-2])
    return values

if __name__ == '__main__':
    result = fibonacci_generator(15)
    print(result)