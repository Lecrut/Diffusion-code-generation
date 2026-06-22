def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    areas = {
        'trapezoid': (5, 7, 4),
        'parallelogram': (6, 3)
    }
    
    total_area = sum(trapezoid_area(*params) if shape == 'trapezoid' else parallelogram_area(*params) for shape, params in areas.items())
    print(total_area)