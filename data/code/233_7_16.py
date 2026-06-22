WIDTH = 5
HEIGHT = 5

def fill_rectangle(width=WIDTH, height=HEIGHT, symbol='*'):
    return (symbol * width for _ in range(height))

if __name__ == '__main__':
    print('\n'.join(fill_rectangle()))