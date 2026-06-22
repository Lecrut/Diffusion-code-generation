def reverse_number_triangle(n):
    for i in range(n, 0, -1):
        print(' '.join(str(j) for j in range(1, i + 1)))

if __name__ == '__main__':
    reverse_number_triangle(5)