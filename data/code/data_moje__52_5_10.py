def render_diamond(size):
    half = size // 2 + 1
    upper = []
    for i in range(half):
        spaces = ' ' * (half - i - 1)
        stars = '* ' * (i + 1)
        upper.append(spaces + stars.strip())
    lower = upper[:-1]
    lower.reverse()
    result = upper + lower
    return '\n'.join(result)

if __name__ == '__main__':
    print(render_diamond(3))