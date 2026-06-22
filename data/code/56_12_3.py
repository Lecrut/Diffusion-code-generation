def generate_multiplication_table(factor, row_count):
    return [factor * i for i in range(1, row_count + 1)]

if __name__ == '__main__':
    table = generate_multiplication_table(3, 10)
    for value in table:
        print(value)