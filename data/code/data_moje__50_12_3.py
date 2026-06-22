def print_hollow_triangle(rows: int) -> str:
    result = []
    for i in range(1, rows + 1):
        if i == 1:
            result.append(" " * (rows - 1) + "*")
        elif i == rows:
            result.append("*" + " " * (rows * 2 - 3) + "*")
        else:
            result.append(" " * (rows - i) + "*" + " " * (2 * i - 3) + "*")
    return "\n".join(result)

if __name__ == "__main__":
    sample_rows = 5
    print(print_hollow_triangle(sample_rows))