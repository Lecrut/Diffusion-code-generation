def generate_fibonacci(count):
    if count <= 0:
        return []
    if count == 1:
        return [0]
    
    fibs = [0, 1]
    for _ in range(2, count):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

if __name__ == '__main__':
    result = generate_fibonacci(20)
    print(result)