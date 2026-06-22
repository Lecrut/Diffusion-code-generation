def calculate_sequence(n):
    return [i**2 + i for i in range(1, n+1)]

if __name__ == '__main__':
    sequence = calculate_sequence(10)
    print(sequence)