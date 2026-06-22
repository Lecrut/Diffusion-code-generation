def generate_multiplication_table(number, rows):
    table = []
    for i in range(1, rows + 1):
        table.append(f"{number} x {i} = {number * i}")
    return table

if __name__ == '__main__':
    result = generate_multiplication_table(3, 10)
    for line in result:
        print(line)