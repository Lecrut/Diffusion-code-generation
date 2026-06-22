def generate_multiplication_table(number):
    table = []
    for i in range(1, 11):
        result = number * i
        table.append(f'{number} x {i} = {result}')
    return table
if __name__ == '__main__':
    number = 5
    table = generate_multiplication_table(number)
    for line in table:
        print(line)