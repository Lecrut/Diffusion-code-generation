def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    sample_number = 100
    result = get_divisors(sample_number)
    print(result)