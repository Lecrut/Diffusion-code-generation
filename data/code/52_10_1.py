def generate_diamond(size: int) -> str:
    if size < 1:
        return ""
    upper_size = size - 1
    lines = []
    for i in range(size):
        stars = "*" * (2 * i + 1)
        spaces = " " * (upper_size - i)
        lines.append(spaces + stars + spaces)
    for i in range(size - 2, -1, -1):
        stars = "*" * (2 * i + 1)
        spaces = " " * (upper_size - i)
        lines.append(spaces + stars + spaces)
    return "\n".join(lines)

if __name__ == "__main__":
    print(generate_diamond(5))