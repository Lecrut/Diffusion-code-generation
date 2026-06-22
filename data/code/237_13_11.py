TRIANGULAR_NUMBER_MULTIPLIER = 1 / 2

if __name__ == '__main__':
    triangular_numbers = [int(n * (n + 1) * TRIANGULAR_NUMBER_MULTIPLIER) for n in range(1, 13)]
    print(triangular_numbers)