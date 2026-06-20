def sum_values(a: int, b: int, c: int) -> int:
    return a + b + c

if __name__ == '__main__':
    values = {
        'x': 10,
        'y': 20,
        'z': 30
    }
    total = sum_values(values['x'], values['y'], values['z'])
    print(total)