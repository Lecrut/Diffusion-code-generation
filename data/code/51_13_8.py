def generate_symmetric_pyramid(rows):
    return "\n".join(
        " " * (rows - i - 1) + "".join(str(j) for j in range(1, i + 1)) + "".join(str(j) for j in range(i - 1, 0, -1))
        for i in range(1, rows + 1)
    )

if __name__ == "__main__":
    row_count = 8
    print(generate_symmetric_pyramid(row_count))