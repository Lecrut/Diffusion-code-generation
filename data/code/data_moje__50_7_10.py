def generate_right_triangle(rows=20):
    result = []
    for i in range(1, rows + 1):
        result.append('*' * i)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_right_triangle(20))