def generate_triangle(rows):
    return [ '*' * i for i in range(1, rows + 1) ]

if __name__ == '__main__':
    result = generate_triangle(20)
    for line in result:
        print(line)