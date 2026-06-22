BOX_SYMBOL = '@'
ROWS = 3
COLS = 2

def print_box():
    for _ in range(ROWS):
        print(BOX_SYMBOL * COLS)

if __name__ == '__main__':
    print_box()