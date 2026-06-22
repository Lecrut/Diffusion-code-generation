def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** 0.5)
    divisor = 3
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2
    return True

if __name__ == '__main__':
    test_values = [1, 2, 3, 4, 5, 9, 23, 57, 97, 100, 121, 127, 200]
    output = []
    for value in test_values:
        result = is_prime(value)
        output.append((value, result))
    for item in output:
        print(item)