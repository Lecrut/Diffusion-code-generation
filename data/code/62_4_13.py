def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

if __name__ == '__main__':
    target_number = 60
    result = get_divisors(target_number)
    print(result)