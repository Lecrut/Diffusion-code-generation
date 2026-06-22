def generate_reverse_number_triangle(rows=5):
    return '\n'.join(''.join(str(j) for j in range(1, i + 1)) for i in range(rows, 0, -1))

if __name__ == '__main__':
    result = generate_reverse_number_triangle()
    print(result)