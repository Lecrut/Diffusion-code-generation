def generate_multiplication_table(n):
    return [n * i for i in range(1, 13)]

if __name__ == '__main__':
    number = 4
    result = generate_multiplication_table(number)
    print(result)