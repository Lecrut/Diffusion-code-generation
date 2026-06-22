def reverse_number_triangle(row_count: int) -> None:
    for i in range(row_count, 0, -1):
        row = ' '.join(str(j) for j in range(i, 0, -1))
        print(row)

if __name__ == '__main__':
    reverse_number_triangle(5)