def print_right_aligned_triangle():
    rows = 10
    result = []
    for i in range(1, rows + 1):
        row_str = " " * (rows - i) + "*" * i
        result.append(row_str)
    return "\n".join(result)

if __name__ == "__main__":
    print(print_right_aligned_triangle())