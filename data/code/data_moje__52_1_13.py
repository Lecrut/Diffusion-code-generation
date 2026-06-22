def print_diamond(height):
    if height % 2 == 0 or height <= 0:
        return ""
    lines = []
    mid = height // 2
    for i in range(mid + 1):
        spaces = mid - i
        stars = 2 * i + 1
        lines.append(" " * spaces + "*" * stars)
    for i in range(mid - 1, -1, -1):
        spaces = mid - i
        stars = 2 * i + 1
        lines.append(" " * spaces + "*" * stars)
    return "\n".join(lines)

if __name__ == "__main__":
    sample_height = 7
    result = print_diamond(sample_height)
    print(result)