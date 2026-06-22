def render_diamond():
    grid_size = 7
    diamond_height = (grid_size + 1) // 2
    for i in range(diamond_height):
        padding = ' ' * (diamond_height - i - 1)
        print(padding + '+ ' * (i * 2 + 1))
    for i in range(diamond_height - 2, -1, -1):
        padding = ' ' * (diamond_height - i - 1)
        print(padding + '+ ' * (i * 2 + 1))

if __name__ == '__main__':
    render_diamond()