def get_multiplication_table(number, count):
    return [f"{number} x {i} = {number * i}" for i in range(1, count + 1)]

if __name__ == '__main__':
    table_rows = get_multiplication_table(3, 10)
    for row in table_rows:
        print(row)