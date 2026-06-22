def non_negative_difference(a, b):
    return abs(a - b)

if __name__ == '__main__':
    values = {'x': 10, 'y': 5}
    print(non_negative_difference(values['x'], values['y']))