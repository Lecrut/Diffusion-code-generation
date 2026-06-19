import math
SHAPE_AREA_FUNCTIONS = {'rectangle': lambda width, height: width * height, 'circle': lambda radius: math.pi * radius ** 2, 'triangle': lambda base, height: 0.5 * base * height}

def calculate_area(shape_type, **kwargs):
    area_function = SHAPE_AREA_FUNCTIONS.get(shape_type)
    if area_function is None:
        raise ValueError(f'Unsupported shape type: {shape_type}')
    required_params = {'rectangle': ['width', 'height'], 'circle': ['radius'], 'triangle': ['base', 'height']}
    missing_params = [param for param in required_params[shape_type] if kwargs.get(param) is None]
    if missing_params:
        raise ValueError(f"Missing required parameters for {shape_type}: {', '.join(missing_params)}")
    return area_function(**kwargs)
if __name__ == '__main__':
    try:
        print(calculate_area('rectangle', width=5, height=10))
        print(calculate_area('circle', radius=7))
        print(calculate_area('triangle', base=6, height=4))
        print(calculate_area('square', side=3))
    except ValueError as e:
        print(e)