def draw_diamond(height):
    mid = (height + 1) // 2
    lines = []
    for i in range(1, height + 1):
        stars = 2 * i - 1 if i <= mid else 2 * (height - i + 1) - 1
        lines.append('*' * stars)
    result = '\n'.join(lines)
    print(result)
    return result

if __name__ == '__main__':
    draw_diamond(7)