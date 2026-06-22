def generate_fibonacci(count):
    result = [0] * count
    if count > 0:
        result[0] = 0
    if count > 1:
        result[1] = 1
    a = 0
    b = 1
    for i in range(2, count):
        a, b = b, a + b
        result[i] = b
    return result

if __name__ == '__main__':
    sequence = generate_fibonacci(75)
    for number in sequence:
        print(number)