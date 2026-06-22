def generate_reverse_triangle(max_rows):
    return [
        " " * (max_rows - i - 1) + str(i + 1) * (i + 1)
        for i in range(max_rows)
    ]

if __name__ == "__main__":
    rows = 5
    result = generate_reverse_triangle(rows)
    for line in result:
        print(line)