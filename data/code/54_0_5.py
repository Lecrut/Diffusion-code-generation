def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    lines = []
    full_row = "*" * size
    lines.append(full_row)
    if size > 1:
        inner_width = size - 2
        middle_row = "*" + " " * inner_width + "*"
        for _ in range(size - 2):
            lines.append(middle_row)
        lines.append(full_row)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_size = 5
    print(generate_hollow_square(sample_size))
    sample_size = 1
    print(generate_hollow_square(sample_size))
    sample_size = 3
    print(generate_hollow_square(sample_size))