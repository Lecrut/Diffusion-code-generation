def render_diamond_pattern(height):
    if height % 2 == 0:
        height = 7
    mid = height // 2
    lines = []
    for i in range(height):
        if i <= mid:
            spaces = mid - i
            stars = 2 * i + 1
        else:
            spaces = i - mid
            stars = 2 * (height - 1 - i) + 1
        line = " " * spaces + "*" * stars
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = render_diamond_pattern(7)
    print(result)