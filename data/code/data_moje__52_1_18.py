def print_diamond(height=7):
    mid = height // 2
    lines = []
    for i in range(height):
        if i <= mid:
            spaces = mid - i
            stars = 2 * i + 1
        else:
            spaces = i - mid
            stars = 2 * (height - i) - 1
        line = ' ' * spaces + '*' * stars
        lines.append(line)
    for line in lines:
        print(line)
    return lines

if __name__ == '__main__':
    result = print_diamond(7)
    print(result)