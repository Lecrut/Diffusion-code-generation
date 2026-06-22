def draw_diamond(radius: int) -> str:
    if radius <= 0:
        return ""
    lines = []
    for i in range(-radius, radius + 1):
        spaces = abs(i)
        stars = (radius - abs(i)) * 2 + 1
        lines.append(" " * spaces + "*" * stars)
    return "\n".join(lines)

if __name__ == "__main__":
    result = draw_diamond(3)
    print(result)