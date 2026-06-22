def fill_rectangle(width=5, height=5, char='*'):
    grid = [[char for _ in range(width)] for _ in range(height)]
    return grid

if __name__ == '__main__':
    sample_values = {'width': 5, 'height': 5, 'char': '*'}
    rectangle = fill_rectangle(**sample_values)
    for row in rectangle:
        print(''.join(row))