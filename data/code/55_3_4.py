def inverted_alphabet_triangle(n: int) -> str:
    if n <= 0:
        return ''
    lines = []
    for i in range(n):
        row_parts = []
        for _ in range(n - i):
            row_parts.append('abcdefghijklmnopqrstuvwxyz')
        row_str = ''.join(row_parts)
        current_length = 26 * (n - i)
        start_char_idx = 0
        end_char_idx = 26 * (n - i)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        width = 26 * (n - i)
        full_row = (alphabet * (width // 26 + 1))[:width]
        lines.append(full_row)
    return '\n'.join(lines)
if __name__ == '__main__':
    print(inverted_alphabet_triangle(2))