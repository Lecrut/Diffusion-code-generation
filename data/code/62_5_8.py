def find_factors(number):
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            yield i
            if i != number // i:
                yield number // i

if __name__ == '__main__':
    target_number = 120
    sorted_factors = sorted(find_factors(target_number))
    print(sorted_factors)