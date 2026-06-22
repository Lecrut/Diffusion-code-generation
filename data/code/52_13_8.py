def print_diamond_pattern(height: int) -> str:
    if height <= 0:
        return ""
    mid = height // 2
    upper = [f"{' ' * (mid - i)}{'*' * (2 * i + 1)}" for i in range(mid + 1)]
    lower = [f"{' ' * (mid - i)}{'*' * (2 * i + 1)}" for i in range(mid - 1, -1, -1)]
    lines = upper + lower
    return "\n".join(lines)

if __name__ == '__main__':
    sample_height = 5
    result = print_diamond_pattern(sample_height)
    print(result)