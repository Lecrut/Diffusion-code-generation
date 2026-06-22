def generate_inverted_triangle(size):
    result = []
    for i in range(size, 0, -1):
        line = '*' * i
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    size = 5
    output = generate_inverted_triangle(size)
    print(output)