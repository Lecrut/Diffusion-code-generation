def print_centered_triangle(size):
    rows = [
        (' ' * (size - i) + '* ' * i).rstrip() for i in range(1, size + 1)
    ]
    for row in rows:
        print(row)

if __name__ == '__main__':
    print_centered_triangle(12)