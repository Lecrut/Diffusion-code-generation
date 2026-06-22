def alphabet_triangle(size):
    if size <= 0 or size > 26:
        size = max(1, min(size, 26))
    lines = []
    for i in range(1, size + 1):
        letters = ''.join((chr(ord('a') + j) for j in range(i)))
        line = letters.rjust(size + (size - i))
        lines.append(line)
    return '\n'.join(lines)
if __name__ == '__main__':
    pattern = alphabet_triangle(5)
    print(pattern)