def generate_right_aligned_pyramid(num_rows):
    rows = []
    for i in range(1, num_rows + 1):
        line = str(i)
        for j in range(2, i + 1):
            line += f" {j}"
        line = line.rjust((num_rows * 3) - 2)
        rows.append(line)
    return "\n".join(rows)

if __name__ == '__main__':
    ROWS = 5
    result = generate_right_aligned_pyramid(ROWS)
    print(result)