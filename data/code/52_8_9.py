def render_diamond_pattern(height: int) -> str:
    if height % 2 == 0:
        return ""
    pattern_lines = []
    mid = height // 2
    for i in range(height):
        if i <= mid:
            stars = 2 * i + 1
            spaces = mid - i
        else:
            stars = 2 * (height - 1 - i) + 1
            spaces = i - mid
        line = " " * spaces + "*" * stars
        pattern_lines.append(line)
    return "\n".join(pattern_lines)

if __name__ == '__main__':
    sample_height = 7
    result = render_diamond_pattern(sample_height)
    print(result)