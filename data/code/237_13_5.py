TRIANGULAR_NUMBER_MULTIPLIER = 0.5

def generate_triangular_numbers(count):
    return [int(TRIANGULAR_NUMBER_MULTIPLIER * n * (n + 1)) for n in range(1, count + 1)]

if __name__ == '__main__':
    triangular_numbers = generate_triangular_numbers(12)
    print(triangular_numbers)