def print_reverse_triangle(n):
    for i in range(n, 0, -1):
        print(" ".join(map(str, range(i, 0, -1))))

if __name__ == '__main__':
    print_reverse_triangle(5)