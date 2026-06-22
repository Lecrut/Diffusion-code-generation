def generate_fibonacci():
    result = []
    a, b = 0, 1
    for _ in range(100):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    print(generate_fibonacci())