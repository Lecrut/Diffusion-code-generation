def generate_diamond_pattern(height):
    if height % 2 == 0:
        height += 1
    mid = height // 2
    lines = [
        ' ' * (mid - i) + '*' * (2 * i + 1)
        for i in range(mid + 1)
    ] + [
        ' ' * (mid - i) + '*' * (2 * i + 1)
        for i in range(mid - 1, -1, -1)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_diamond_pattern(7)
    print(result)