def generate_star_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        result.append('*' * i)
    return '\n'.join(result)

if __name__ == '__main__':
    NUM_ROWS = 20
    output = generate_star_triangle(NUM_ROWS)
    print(output)