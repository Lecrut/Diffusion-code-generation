def print_reverse_number_triangle(height: int = 5) -> None:
    for i in range(height, 0, -1):
        row = ' '.join(str(j) for j in range(i, 0, -1))
        print(row)

if __name__ == '__main__':
    print_reverse_number_triangle()