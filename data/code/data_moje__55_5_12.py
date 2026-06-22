def render_diamond(height: int) -> str:
    if height <= 0:
        return ""
    if height == 1:
        return "A"
    lines = []
    mid = height - 1
    for i in range(height):
        if i <= mid:
            current_char_code = 65 + i
            spaces = " " * (mid - i)
            left_part = "".join(chr(65 + j) for j in range(i + 1))
            right_part = "".join(chr(65 + j) for j in range(i - 1, -1, -1))
            line = spaces + left_part + right_part
        else:
            mirror_index = mid - (i - mid)
            current_char_code = 65 + mirror_index
            spaces = " " * (mid - mirror_index)
            left_part = "".join(chr(65 + j) for j in range(mirror_index + 1))
            right_part = "".join(chr(65 + j) for j in range(mirror_index - 1, -1, -1))
            line = spaces + left_part + right_part
        lines.append(line)
    for i in range(mid - 1, -1, -1):
        current_char_code = 65 + i
        spaces = " " * (mid - i)
        left_part = "".join(chr(65 + j) for j in range(i + 1))
        right_part = "".join(chr(65 + j) for j in range(i - 1, -1, -1))
        lines.append(spaces + left_part + right_part)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_height = 5
    result = render_diamond(sample_height)
    print(result)