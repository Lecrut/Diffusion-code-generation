def reverse_number_triangle(n):
    return '\n'.join(' '.join(str(i) for i in range(1, n - row + 1)) for row in range(n, 0, -1))

if __name__ == '__main__':
    print(reverse_number_triangle(5))