def generate_reverse_triangle(rows):
    return '\n'.join(' '.join(str(j) for j in range(i, 0, -1)) for i in range(rows, 0, -1))

if __name__ == '__main__':
    print(generate_reverse_triangle(5))