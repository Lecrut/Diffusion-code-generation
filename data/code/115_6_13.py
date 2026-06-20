def divide_pairs(dividends, divisors):
    for dividend, divisor in zip(dividends, divisors):
        yield dividend / divisor

if __name__ == '__main__':
    dividends = [10, 20, 30]
    divisors = [2, 4, 5]
    results = divide_pairs(dividends, divisors)
    for result in results:
        print(result)