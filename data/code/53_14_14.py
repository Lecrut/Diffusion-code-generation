def reverse_number_triangle(n):
    return '\n'.join(' '.join(str(n - i + j) for j in range(1, n - i + 1)) for i in range(n))

if __name__ == '__main__':
    print(reverse_number_triangle(5))