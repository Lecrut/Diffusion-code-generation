def generate_hollow_rectangle(width, height):
    if width < 2 or height < 2:
        return []

    top_bottom = '*' * width
    sides = ['*' + ' ' * (width - 2) + '*'] * (height - 2)

    return [top_bottom] + sides + [top_bottom]

if __name__ == '__main__':
    pattern = generate_hollow_rectangle(6, 4)
    for line in pattern:
        print(line)