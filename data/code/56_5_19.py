def generate_multiplication_grid():
    return [[i * j for j in range(1, 11)] for i in range(1, 11)]

if __name__ == '__main__':
    result = generate_multiplication_grid()
    for row in result:
        print(row)