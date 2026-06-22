def generate_reverse_number_triangle(n):
    return '\n'.join(''.join(str(j) for j in range(1, i + 1)) for i in range(n, 0, -1))

if __name__ == '__main__':
    print(generate_reverse_number_triangle(5))