def generate_diamond_pattern(size: int) -> str:
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    top_lines = []
    for i in range(size):
        spaces = " " * (size - 1 - i)
        stars = "*" * (2 * i + 1)
        top_lines.append(spaces + stars)
    bottom_lines = []
    for i in range(size - 2, -1, -1):
        spaces = " " * (size - 1 - i)
        stars = "*" * (2 * i + 1)
        bottom_lines.append(spaces + stars)
    return "\n".join(top_lines + bottom_lines)

if __name__ == "__main__":
    sample_size = 5
    result = generate_diamond_pattern(sample_size)
    print(result)