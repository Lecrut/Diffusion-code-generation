def print_reverse_number_triangle(height=5):
    for i in range(height, 0, -1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        print(" ".join(row))

if __name__ == '__main__':
    print_reverse_number_triangle()