def generate_multiplication_grid():
    return [[x * y for y in range(1, 11)] for x in range(1, 11)]

if __name__ == '__main__':
    result = generate_multiplication_grid()
    for row in result:
        print(row)