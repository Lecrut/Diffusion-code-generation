def generate_zigzag_triangle(rows: int) -> list[str]:
    result = []
    current_row = 1
    for i in range(rows):
        line = []
        for j in range(i + 1):
            if (current_row + j) % 2 == 0:
                char = chr(ord('A') + (current_row + j) % 26)
            else:
                char = chr(ord('a') + (current_row + j) % 26)
            line.append(char)
        result.append("".join(line))
        current_row += i + 1
    return result

if __name__ == '__main__':
    triangle = generate_zigzag_triangle(5)
    for row in triangle:
        print(row)