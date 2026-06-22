NUM_ROWS = 5

def draw_diamond():
    for i in range(NUM_ROWS):
        spaces = ' ' * (NUM_ROWS - i - 1)
        bars = '|' * (2 * i + 1)
        print(spaces + bars)

if __name__ == '__main__':
    draw_diamond()