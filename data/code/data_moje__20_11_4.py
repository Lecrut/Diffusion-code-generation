def check_evenness(n: int) -> bool:
    return n % 2 == 0
if __name__ == '__main__':
    test_values = [-4, -3, 0, 1, 2, 3, 100, -100]
    for value in test_values:
        print(f'{value} is even: {check_evenness(value)}')