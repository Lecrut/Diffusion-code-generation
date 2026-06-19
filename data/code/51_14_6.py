SQUARE_CONFIG = {
    'side_length': 9
}

def calculate_perimeter(config):
    side_length = config['side_length']
    return 4 * side_length

if __name__ == '__main__':
    perimeter = calculate_perimeter(SQUARE_CONFIG)
    print(perimeter)