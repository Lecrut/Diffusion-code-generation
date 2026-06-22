def generate_multiplication_table(number, rows):
    return [f"{number} x {i} = {number * i}" for i in range(1, rows + 1)]

if __name__ == '__main__':
    table = generate_multiplication_table(3, 10)
    for line in table:
        print(line)