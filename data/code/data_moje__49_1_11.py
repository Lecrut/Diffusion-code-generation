def print_star_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*\n"
    lines = []
    lines.append("*" * size)
    for _ in range(size - 2):
        lines.append("*" + " " * (size - 2) + "*")
    lines.append("*" * size)
    return "\n".join(lines) + "\n"

if __name__ == "__main__":
    print(print_star_square(5), end="")
    print(print_star_square(1), end="")
    print(print_star_square(3), end="")