import sys
WIDTH = 10
HEIGHT = 10
def generate_square(w, h):
    grid = []
    for y in range(h):
        row = []
        for x in range(w):
            if x == w // 2 and y == h // 2:
                row.append('X')
            else:
                row.append(' ')
        grid.append("".join(row))
    return "\n".join(grid)
if __name__ == '__main__':
    print(generate_square(WIDTH, HEIGHT))