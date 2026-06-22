def render_diamond(height):
    if height % 2 == 0:
        return []
    result = []
    mid = height // 2
    for i in range(height):
        if i <= mid:
            spaces = mid - i
            stars = 2 * i + 1
        else:
            spaces = i - mid
            stars = 2 * (height - 1 - i) + 1
        result.append(" " * spaces + "*" * stars)
    return result

if __name__ == '__main__':
    height = 7
    lines = render_diamond(height)
    for line in lines:
        print(line)