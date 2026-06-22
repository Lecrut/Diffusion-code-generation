def print_diamond(height):
    if height % 2 == 0:
        height += 1
    mid = height // 2
    rows = [' ' * (mid - i) + '*' * (2 * i + 1) + ' ' * (mid - i) for i in range(mid + 1)]
    rows += [' ' * (mid - i) + '*' * (2 * i + 1) + ' ' * (mid - i) for i in range(mid - 1, -1, -1)]
    return '\n'.join(rows)
if __name__ == '__main__':
    sample_height = 7
    result = print_diamond(sample_height)
    print(result)