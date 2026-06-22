def generate_multiplication_table_7():
    return '\n'.join(f'{i} x 7 = {i * 7}' for i in range(1, 11))

if __name__ == '__main__':
    print(generate_multiplication_table_7())