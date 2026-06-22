NUM_ROWS = 4

def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

if __name__ == '__main__':
    print_right_triangle(NUM_ROWS)