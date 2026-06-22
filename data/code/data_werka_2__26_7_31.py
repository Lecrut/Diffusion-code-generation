def compare_greater(x, y):
    return x > y

if __name__ == '__main__':
    values = {'x': 15, 'y': 10}
    print(compare_greater(values['x'], values['y']))
    print(compare_greater(2, 8))