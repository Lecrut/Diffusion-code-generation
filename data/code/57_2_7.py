def calculate_area(shape_type, **kwargs):
    shape_functions = {'triangle': lambda base, height: 0.5 * base * height}
    if shape_type in shape_functions:
        func = shape_functions[shape_type]
        return func(**kwargs)
    else:
        raise ValueError(f'Unsupported shape type: {shape_type}')
if __name__ == '__main__':
    base = 8.0
    height = 3.5
    triangle_area = calculate_area('triangle', base=base, height=height)
    print(triangle_area)