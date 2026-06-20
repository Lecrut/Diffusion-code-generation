def basic_arithmetic(x, y):
    results = {
        'addition': x + y,
        'subtraction': x - y,
        'multiplication': x * y,
        'floor_division': x // y
    }
    return results

if __name__ == '__main__':
    sample_x, sample_y = 15, 3
    output = basic_arithmetic(sample_x, sample_y)
    print(output)