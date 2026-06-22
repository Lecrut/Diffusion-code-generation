def calculate_sequence(n):
    return [i**2 + i for i in range(1, n+1)]

if __name__ == '__main__':
    sample_value = 10
    result = calculate_sequence(sample_value)
    print(result)