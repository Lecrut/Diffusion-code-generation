def calculate_area(shape_type, **kwargs):
    shape_functions = {'triangle': lambda base, height: 0.5 * base * height}
    if shape_type in shape_functions:
        func = shape_functions[shape_type]
        return func(**kwargs)
    else:
        raise ValueError('Unsupported shape type')
if __name__ == '__main__':
    base = 10.0
    height = 5.0
    triangle_area = calculate_area('triangle', base=base, height=height)
    print(f'Triangle Area: {triangle_area}')