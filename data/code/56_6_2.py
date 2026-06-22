def generate_multiplication_table_rows(number, count):
    for i in range(1, count + 1):
        yield f"{number} x {i} = {number * i}"

if __name__ == '__main__':
    number = 9
    count = 10
    rows = generate_multiplication_table_rows(number, count)
    for row in rows:
        print(row)