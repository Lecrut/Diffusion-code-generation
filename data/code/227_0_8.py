def print_right_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

if __name__ == '__main__':
    NUM_ROWS = 5
    print_right_triangle(NUM_ROWS)