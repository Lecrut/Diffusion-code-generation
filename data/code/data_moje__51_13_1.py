def generate_symmetric_pyramid(rows: int) -> list[str]:
    result = []
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        left_part = "".join(str(j) for j in range(1, i + 1))
        right_part = "".join(str(j) for j in range(i - 1, 0, -1))
        line = spaces + left_part + right_part
        result.append(line)
    return result

if __name__ == '__main__':
    pattern = generate_symmetric_pyramid(8)
    for line in pattern:
        print(line)