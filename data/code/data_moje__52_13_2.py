def generate_diamond(height):
    lines = []
    mid = height // 2
    for i in range(-mid, mid + 1):
        spaces = abs(mid - abs(i))
        stars = height - 2 * spaces
        lines.append(" " * spaces + "* " * stars)
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_diamond(5))