def generate_nine_multiplication_table():
    return [f"9 * {i} = {9 * i}" for i in range(1, 11)]

if __name__ == '__main__':
    print(generate_nine_multiplication_table())