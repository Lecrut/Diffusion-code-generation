def print_multiplication_table(n):
    print('\n'.join(f'{n} x {i} = {n * i}' for i in range(1, 11)))

if __name__ == '__main__':
    print_multiplication_table(5)