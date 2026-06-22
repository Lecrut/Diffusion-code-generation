def print_diamond(height: int = 7) -> str:
    if height % 2 == 0:
        raise ValueError("Height must be an odd number to form a symmetric diamond.")
    mid = height // 2
    lines = []
    for i in range(height):
        if i <= mid:
            num_stars = 2 * i + 1
            num_spaces = mid - i
        else:
            num_stars = 2 * (height - 1 - i) + 1
            num_spaces = i - mid
        line = " " * num_spaces + "*" * num_stars
        lines.append(line)
    diamond_str = "\n".join(lines)
    print(diamond_str)
    return diamond_str

if __name__ == '__main__':
    result = print_diamond(7)
    print(repr(result))