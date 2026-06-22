def render_hollow_square(size: int, char: str = "*") -> str:
    if size <= 0:
        return ""
    if size == 1:
        return char
    top_bottom = char * size
    middle = char + " " * (size - 2) + char
    lines = [top_bottom]
    for _ in range(size - 2):
        lines.append(middle)
    lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == "__main__":
    sample_size = 7
    result = render_hollow_square(sample_size, "#")
    print(result)