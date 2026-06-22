if __name__ == '__main__':
    NUM_TERMS = 12
    triangular_numbers = [n * (n + 1) // 2 for n in range(1, NUM_TERMS + 1)]
    print(triangular_numbers)