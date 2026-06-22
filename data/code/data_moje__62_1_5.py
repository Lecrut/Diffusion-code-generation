def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    number = 100
    result = get_divisors(number)
    print(result)