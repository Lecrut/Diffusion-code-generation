def generate_multiplication_table(n):
    return '\n'.join(f"{i} x {n} = {i * n}" for i in range(1, 11))

if __name__ == '__main__':
    print(generate_multiplication_table(7))