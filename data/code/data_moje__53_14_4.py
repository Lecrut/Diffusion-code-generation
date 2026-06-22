def generate_reverse_triangle(n):
    return '\n'.join(' '.join(str(n - i - j) for j in range(n - i)) for i in range(n))

if __name__ == '__main__':
    print(generate_reverse_triangle(5))