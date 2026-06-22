def print_diamond(height):
    if height <= 0:
        return ""
    half = height // 2 + 1 if height % 2 != 0 else height // 2
    upper = [
        (" " * (half - 1 - i)) + ("*" * (2 * i + 1))
        for i in range(half)
    ]
    if height % 2 == 0:
        half -= 1
    lower = [
        (" " * (half - 1 - i)) + ("*" * (2 * i + 1))
        for i in range(half - 1, -1, -1)
    ]
    pattern = upper + lower
    return "\n".join(pattern)

if __name__ == '__main__':
    sample_height = 7
    result = print_diamond(sample_height)
    print(result)