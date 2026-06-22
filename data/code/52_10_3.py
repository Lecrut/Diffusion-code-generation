def generate_diamond(size: int) -> str:
    if size <= 0:
        return ""
    lines = []
    for i in range(size):
        spaces = " " * (size - 1 - i)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    for i in range(size - 2, -1, -1):
        spaces = " " * (size - 1 - i)
        stars = "*" * (2 * i + 1)
        lines.append(spaces + stars)
    return "\n".join(lines)

if __name__ == "__main__":
    sample_size = 5
    print(generate_diamond(sample_size))