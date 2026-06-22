def generate_fibonacci(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    result = [0, 1]
    for _ in range(2, count):
        result.append(result[-1] + result[-2])
    return result

if __name__ == '__main__':
    fibs = generate_fibonacci(200)
    print(fibs)