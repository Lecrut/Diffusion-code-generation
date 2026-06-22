def generate_hollow_alphabet_triangle(n: int) -> list[str]:
    if n <= 0:
        return []
    rows = []
    for i in range(1, n + 1):
        spaces_before = ' ' * (n - i)
        if i == 1:
            chars = 'A'
        elif i == n:
            chars = ''.join((chr(ord('A') + j % 26) for j in range(i)))
        elif i == 2:
            chars = 'A' + 'B'
        else:
            start_char_idx = (i - 1) % 26
            start_char = chr(ord('A') + start_char_idx)
            row_chars = [start_char]
            if i > 2:
                row_chars.extend([' '] * (i - 2))
            if i > 1:
                row_chars.append(start_char)
            chars = ''.join(row_chars)
        row_str = chars
        rows.append(row_str)
    return rows

def print_hollow_alphabet_triangle(n: int) -> None:
    pattern = generate_hollow_alphabet_triangle(n)
    for row in pattern:
        print(row)
if __name__ == '__main__':
    base_width = 5
    result = generate_hollow_alphabet_triangle(base_width)
    for row in result:
        print(row)