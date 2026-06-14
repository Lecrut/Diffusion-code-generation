def fill_rectangle(width, height, char):
    grid = []
    for _ in range(height):
        row = [char] * width
        grid.append(row)
    return grid
if __name__ == '__main__':
    w = 5
    h = 3
    c = '#'
    result = fill_rectangle(w, h, c)
    for row in result:
        print("".join(row))