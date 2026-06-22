def generate_fibonacci(count):
    if count <= 0:
        return []
    result = [0] * count
    if count > 1:
        result[1] = 1
    for i in range(2, count):
        result[i] = result[i - 1] + result[i - 2]
    return result

if __name__ == '__main__':
    numbers = generate_fibonacci(75)
    for n in numbers:
        print(n)