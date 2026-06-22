def print_right_triangle(rows):
    MAX_ROWS = 5
    if rows > MAX_ROWS:
        rows = MAX_ROWS
    
    for i in range(1, rows + 1):
        print('*' * i)

if __name__ == '__main__':
    print_right_triangle(5)