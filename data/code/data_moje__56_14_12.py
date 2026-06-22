def generate_multiplication_table(base_value):
    return [base_value * i for i in range(1, 11)]

if __name__ == '__main__':
    table = generate_multiplication_table(4)
    print(table)