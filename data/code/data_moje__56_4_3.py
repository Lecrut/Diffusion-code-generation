def print_multiplication_table():
    print('\n'.join(f'5 * {i} = {5 * i}' for i in range(1, 11)))

if __name__ == '__main__':
    print_multiplication_table()