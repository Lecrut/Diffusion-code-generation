def generate_multiplication_table(n=7):
    return '\n'.join(f"{n} x {i} = {n * i}" for i in range(1, 11))

if __name__ == '__main__':
    print(generate_multiplication_table())