def generate_multiplication_table(n):
    return [n * i for i in range(1, 11)]

if __name__ == '__main__':
    sample_value = 5
    result = generate_multiplication_table(sample_value)
    print(result)