def print_reverse_number_triangle(height: int = 5) -> None:
    for row in range(1, height + 1):
        line = " ".join(str(j) for j in range(row, 0, -1))
        print(line)

if __name__ == "__main__":
    print_reverse_number_triangle(5)