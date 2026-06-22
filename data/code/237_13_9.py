TRIANGULAR_NUMBER_COUNT = 12

if __name__ == '__main__':
    triangular_numbers = [n * (n + 1) // 2 for n in range(TRIANGULAR_NUMBER_COUNT)]
    print(triangular_numbers)