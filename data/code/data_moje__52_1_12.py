def generate_diamond(height):
    lines = []
    mid = height // 2
    for i in range(height):
        if i <= mid:
            spaces = mid - i
            stars = 2 * i + 1
        else:
            spaces = i - mid
            stars = 2 * (height - i - 1) + 1
        line = ' ' * spaces + '*' * stars + ' ' * spaces
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    height = 7
    result = generate_diamond(height)
    print(result)