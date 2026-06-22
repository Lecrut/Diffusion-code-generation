def compute_diamond_rows(count):
    config = {
        'up_start': 1,
        'up_stop': count + 1,
        'up_step': 1,
        'down_start': count - 1,
        'down_stop': 0,
        'down_step': -1,
        'spacer': ' ',
        'marker': '*'
    }
    rows = []
    range_up = range(config['up_start'], config['up_stop'], config['up_step'])
    range_down = range(config['down_start'], config['down_stop'], config['down_step'])
    
    for i in range_up:
        spaces = config['spacer'] * (count - i)
        stars = config['marker'] * (2 * i - 1)
        rows.append(spaces + stars)
        
    for i in range_down:
        spaces = config['spacer'] * (count - i)
        stars = config['marker'] * (2 * i - 1)
        rows.append(spaces + stars)
        
    return rows

if __name__ == '__main__':
    SIZE = 8
    output_lines = compute_diamond_rows(SIZE)
    for line in output_lines:
        print(line)