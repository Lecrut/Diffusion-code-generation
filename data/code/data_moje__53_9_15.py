def print_reverse_number_triangle(height: int = 5) -> None:
    for i in range(height, 0, -1):
        row = " ".join(str(i) for _ in range(i))
        print(row)

if __name__ == '__main__':
    print_reverse_number_triangle(5)