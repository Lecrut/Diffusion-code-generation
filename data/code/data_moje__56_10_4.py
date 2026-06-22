def generate_multiplication_table(number, limit):
    return [f"{number} x {i} = {number * i}" for i in range(1, limit + 1)]

if __name__ == '__main__':
    specific_number = 5
    table = generate_multiplication_table(specific_number, 10)
    for line in table:
        print(line)