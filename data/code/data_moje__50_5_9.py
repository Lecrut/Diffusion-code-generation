def generate_triangle(rows):
    result = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + '* ' * i
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    count = 9
    print(generate_triangle(count))