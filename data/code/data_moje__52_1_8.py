def print_diamond(height=7):
    if height % 2 == 0:
        height += 1
    mid = height // 2
    lines = []
    for i in range(height):
        if i <= mid:
            num_stars = 2 * i + 1
            spaces = mid - i
        else:
            num_stars = 2 * (height - 1 - i) + 1
            spaces = i - mid
        line = ' ' * spaces + '*' * num_stars
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_diamond(7)
    print(result)