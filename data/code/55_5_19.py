def render_diamond(height):
    if height <= 0:
        return ""
    if height % 2 == 0:
        height += 1
    mid = height // 2 + 1
    lines = []
    for i in range(1, mid + 1):
        prefix = ' ' * (mid - i)
        letters = []
        for j in range(i):
            idx = j
            letters.append(chr(ord('A') + idx))
        for j in range(i - 2, -1, -1):
            idx = j
            letters.append(chr(ord('A') + idx))
        line = prefix + ''.join(letters)
        lines.append(line)
    for i in range(mid - 1, 0, -1):
        prefix = ' ' * (mid - i)
        letters = []
        for j in range(i):
            idx = j
            letters.append(chr(ord('A') + idx))
        for j in range(i - 2, -1, -1):
            idx = j
            letters.append(chr(ord('A') + idx))
        line = prefix + ''.join(letters)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = render_diamond(5)
    print(result)