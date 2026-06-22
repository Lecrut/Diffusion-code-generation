def generate_multiplication_table(number, rows):
    return [f"{number} x {i} = {number * i}" for i in range(1, rows + 1)]

if __name__ == '__main__':
    number = 3
    rows = 10
    table_lines = generate_multiplication_table(number, rows)
    for line in table_lines:
        print(line)