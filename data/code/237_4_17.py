def triangular_numbers():
    return [n * (n + 1) // 2 for n in range(1, 13)]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(triangular_numbers())