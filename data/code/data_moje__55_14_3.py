def generate_centered_alphabet_triangle(rows: int) -> list[str]:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(1, rows + 1):
        letters = alphabet[:i]
        spaces = " " * (rows - i)
        line = spaces + letters + spaces
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    triangle_lines = generate_centered_alphabet_triangle(sample_rows)
    for line in triangle_lines:
        print(line)