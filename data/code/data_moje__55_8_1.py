def generate_zigzag_triangle(rows: int) -> list[str]:
    if rows <= 0:
        return []
    result = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    current_char = 0
    for i in range(1, rows + 1):
        line = []
        for j in range(1, i + 1):
            line.append(alphabet[current_char % 26])
            current_char += 1
        if i % 2 == 0:
            line.reverse()
        result.append(" ".join(line))
    return result

if __name__ == '__main__':
    n = 5
    lines = generate_zigzag_triangle(n)
    for line in lines:
        print(line)