def generate_reverse_triangle(n):
    return '\n'.join(' '.join(str(i) for i in range(j, n + 1)) for j in range(1, n + 1))

if __name__ == '__main__':
    print(generate_reverse_triangle(5))