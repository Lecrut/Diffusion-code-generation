def generate_multiplication_table(number):
    return [f'{number} x {i} = {number * i}' for i in range(1, 11)]

def print_multiplication_table(number):
    table = generate_multiplication_table(number)
    for line in table:
        print(line)
if __name__ == '__main__':
    print_multiplication_table(5)