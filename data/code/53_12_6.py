def create_reverse_number_triangle(rows):
    return "\n".join(" ".join(str(n) for n in range(row, 0, -1)) for row in range(rows, 0, -1))

if __name__ == '__main__':
    sample_rows = 5
    print(create_reverse_number_triangle(sample_rows))