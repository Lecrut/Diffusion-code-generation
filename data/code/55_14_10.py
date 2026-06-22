def generate_centered_alphabet_triangle(rows: int) -> list:
    if rows <= 0:
        return []
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if rows > len(alphabet):
        rows = len(alphabet)
    
    result = []
    for i in range(1, rows + 1):
        row_chars = alphabet[:i]
        spacing = " " * (rows - i)
        line = spacing + " ".join(row_chars) + spacing
        result.append(line)
    
    return result

if __name__ == '__main__':
    sample_rows = 5
    triangle_lines = generate_centered_alphabet_triangle(sample_rows)
    for line in triangle_lines:
        print(line)