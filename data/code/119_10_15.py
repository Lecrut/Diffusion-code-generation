def swap_values(a, b):
    return b, a

if __name__ == '__main__':
    values = {'x': 5, 'y': 10}
    x, y = swap_values(values['x'], values['y'])
    print(f"x: {x}, y: {y}")