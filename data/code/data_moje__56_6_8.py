def generate_multiplication_table_row(number, count):
    for i in range(1, count + 1):
        yield i * number

if __name__ == '__main__':
    number = 9
    count = 10
    for value in generate_multiplication_table_row(number, count):
        print(value)