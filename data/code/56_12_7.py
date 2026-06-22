def generate_multiplication_table(number, rows_count):
    return [f"{number} x {i} = {number * i}" for i in range(1, rows_count + 1)]

if __name__ == '__main__':
    result = generate_multiplication_table(3, 10)
    for row in result:
        print(row)