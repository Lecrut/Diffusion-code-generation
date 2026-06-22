def generate_multiplication_table(number, limit=10):
    table = []
    for i in range(1, limit + 1):
        result = number * i
        table.append(f'{number} * {i} = {result}')
    return table
if __name__ == '__main__':
    target_number = 5
    multiplication_table = generate_multiplication_table(target_number)
    for line in multiplication_table:
        print(line)