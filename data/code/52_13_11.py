def print_diamond(height):
    if height % 2 == 0:
        height += 1
    mid = height // 2
    lines = [' ' * (mid - i) + '*' * (2 * i + 1) for i in range(mid + 1)]
    lines += [' ' * (i + 1) + '*' * (2 * (mid - i - 1) + 1) for i in range(mid)]
    return '\n'.join(lines)
if __name__ == '__main__':
    sample_height = 7
    result = print_diamond(sample_height)
    print(result)