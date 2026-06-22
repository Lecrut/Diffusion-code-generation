def draw_hollow_triangle():
    size = 8
    rows = []
    for i in range(1, size + 1):
        if i == size:
            line = '*' * (2 * i - 1)
        elif i == 1:
            line = '*'
        else:
            stars_outside = i - 1
            spaces_inside = (2 * i - 1) - 2 * stars_outside
            line = '*' * stars_outside + ' ' * spaces_inside + '*'
        rows.append(line)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(draw_hollow_triangle())