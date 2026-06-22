def render_diamond(height=7):
    result = []
    mid = height // 2
    for i in range(height):
        if i <= mid:
            spaces = mid - i
            stars = 2 * i + 1
        else:
            spaces = i - mid
            stars = 2 * (height - i) - 1
        row = ' ' * spaces + '*' * stars
        result.append(row)
    return '\n'.join(result)

if __name__ == '__main__':
    print(render_diamond(7))