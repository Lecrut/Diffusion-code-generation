def check_number(n):
    checks = {
        'positive': n > 0,
        'even': n % 2 == 0,
        'divisible_by_three': n % 3 == 0
    }
    return checks

if __name__ == '__main__':
    sample_numbers = [10, 15, -4, 6]
    for number in sample_numbers:
        results = check_number(number)
        print(f"Number: {number}, Positive: {results['positive']}, Even: {results['even']}, Divisible by 3: {results['divisible_by_three']}")