def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, 16, 17, 97, 98, 99, 100]
    for value in sample_values:
        print(f"{value}: {is_prime(value)}")