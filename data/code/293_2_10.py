def calculate_area(shape, *params):
    if shape == 'circle':
        radius = params[0]
        return 3.14159 * radius ** 2
    elif shape == 'square':
        side = params[0]
        return side ** 2
    elif shape == 'rectangle':
        length, width = params
        return length * width
    else:
        raise ValueError('Unsupported shape')
if __name__ == '__main__':
    print(calculate_area('circle', 5))
    print(calculate_area('square', 4))
    print(calculate_area('rectangle', 3, 2))