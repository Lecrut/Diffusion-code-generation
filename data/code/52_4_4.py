def generate_diamond_pattern(center_width: int) -> str:
    half = center_width // 2
    lines = [" " * (half - i) + "*" * (2 * i + 1) for i in range(half + 1)]
    lines += [" " * (half - i) + "*" * (2 * i + 1) for i in range(half - 1, -1, -1)]
    return "\n".join(lines)

if __name__ == "__main__":
    pattern = generate_diamond_pattern(9)
    print(pattern)