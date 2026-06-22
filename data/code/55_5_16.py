def render_diamond_pattern(height: int) -> str:
    if height <= 0:
        return ""
    if height % 2 == 0:
        height += 1
    mid = height // 2
    lines = []
    for i in range(height):
        if i <= mid:
            distance = mid - i
        else:
            distance = i - mid
        spaces = " " * distance
        count = height - 2 * distance
        start_char_idx = (26 - count) // 2
        chars = [chr(ord('A') + (start_char_idx + j) % 26) for j in range(count)]
        line = spaces + "".join(chars) + spaces
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_height = 5
    result = render_diamond_pattern(sample_height)
    print(result)