def print_asterisk_grid(size):
    SEPARATOR = '|'
    VERTICAL_LINE = ' | '
    
    for i in range(size):
        row = [SEPARATOR + '*' * size + SEPARATOR]
        print(*row)
        
if __name__ == '__main__':
    grid_size = 15
    print_asterisk_grid(grid_size)