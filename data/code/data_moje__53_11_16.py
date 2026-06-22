def print_reverse_number_triangle(height: int) -> None:
    for i in range(height, 0, -1):
        line = ""
        for j in range(i, 0, -1):
            line += str(j) + " "
        print(line.strip())

if __name__ == "__main__":
    triangle_height = 5
    print_reverse_number_triangle(triangle_height)