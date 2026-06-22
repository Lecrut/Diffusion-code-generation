def generate_multiplication_table(number):
    return '\n'.join(f'{number} x {i} = {number * i}' for i in range(1, 11))

if __name__ == '__main__':
    print(generate_multiplication_table(7))