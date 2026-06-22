def generate_number_pyramid(levels: int) -> str:
    lines = []
    current_number = 1
    for level in range(1, levels + 1):
        row_values = []
        for _ in range(level):
            row_values.append(str(current_number))
            current_number += 1
        spaces = " " * (levels - level)
        lines.append(spaces + " ".join(row_values))
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_number_pyramid(4)
    print(result)