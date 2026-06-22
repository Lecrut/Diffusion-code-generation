import itertools

def generate_symbol_block(width, height, symbol):
    coordinates = list(itertools.product(range(height), range(width)))
    return '\n'.join(' '.join(symbol if (x == 0 or x == width - 1 or y == 0 or y == height - 1) else ' ' for x in range(width)) for y, _ in coordinates)

if __name__ == '__main__':
    sample_width = 8
    sample_height = 6
    sample_symbol = '#'
    
    block = generate_symbol_block(sample_width, sample_height, sample_symbol)
    print(block)