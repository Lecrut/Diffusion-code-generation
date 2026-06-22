def get_divisors(number):
    if number == 0:
        return []
    if number < 0:
        number = -number
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    test_values = [0, 1, 10, 15, -20]
    for val in test_values:
        result = get_divisors(val)
        print(f"Divisors of {val}: {result}")