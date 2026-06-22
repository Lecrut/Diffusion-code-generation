def create_hollow_square(size: int = 10) -> str:
    if size <= 0:
        return ""
    border = "*" * size
    inner = "*" + " " * (size - 2) + "*"
    lines = []
    lines.append(border)
    for _ in range(size - 2):
        lines.append(inner)
    if size > 1:
        lines.append(border)
    return "\n".join(lines)

if __name__ == "__main__":
    result = create_hollow_square(10)
    print(result)