def sum_three(a, b, c):
    return a + b + c

if __name__ == '__main__':
    values = {'x': 10, 'y': 20, 'z': 30}
    result = sum_three(values['x'], values['y'], values['z'])
    print(result)