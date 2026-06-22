def generate_multiplication_table(number):
    table = []
    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}")
    return table

if __name__ == '__main__':
    target_number = 5
    result = generate_multiplication_table(target_number)
    for line in result:
        print(line)