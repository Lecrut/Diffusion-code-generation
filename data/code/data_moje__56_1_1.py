def generate_multiplication_table():
    table = []
    for i in range(1, 13):
        row = []
        for j in range(1, 13):
            row.append(f'{i * j:4}')
        table.append(''.join(row))
    return '\n'.join(table)
if __name__ == '__main__':
    print(generate_multiplication_table())