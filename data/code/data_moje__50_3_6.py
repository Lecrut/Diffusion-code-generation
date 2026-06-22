def generate_triangle(rows):
    result = []
    for i in range(rows):
        result.append('*' * (i + 1))
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_triangle(15))