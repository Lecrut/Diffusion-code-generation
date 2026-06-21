def check_even(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [2, 3, 4, 5, 0, -2]
    results = []
    for val in sample_values:
        results.append(check_even(val))
    print(results)