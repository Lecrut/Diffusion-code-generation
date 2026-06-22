def generate_multiplication_table(n):
    return [n * i for i in range(1, 11)]

if __name__ == '__main__':
    sample_number = 5
    result = generate_multiplication_table(sample_number)
    print(result)