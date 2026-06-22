def print_star_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    lines = []
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    lines.append(top_bottom)
    for _ in range(size - 2):
        lines.append(middle)
    lines.append(top_bottom)
    return "\n".join(lines)

if __name__ == '__main__':
    print(print_star_square(5))
    print(print_star_square(4))
    print(print_star_square(1))
    print(print_star_square(3))