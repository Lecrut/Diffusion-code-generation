def generate_number_pyramid(levels: int) -> str:
    lines = []
    for row in range(1, levels + 1):
        numbers = list(range(1, row + 1))
        numbers += list(range(row - 1, 0, -1))
        line = " ".join(map(str, numbers))
        padding = " " * (levels - row)
        lines.append(padding + line + padding)
    return "\n".join(lines)

if __name__ == "__main__":
    print(generate_number_pyramid(4))