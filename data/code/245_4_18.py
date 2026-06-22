from typing import Tuple
PARALLELOGRAM_AREA = 'Parallelogram Area'
TRAPEZOID_AREA = 'Trapezoid Area'

def calculate_area(shape: str, base: float, height: float, side_a: float=None, side_b: float=None) -> Tuple[float, str]:
    if shape == 'parallelogram':
        area = base * height
        return (area, PARALLELOGRAM_AREA)
    elif shape == 'trapezoid':
        area = 0.5 * (base + side_a) * height
        return (area, TRAPEZOID_AREA)
    else:
        raise ValueError('Invalid shape specified')
if __name__ == '__main__':
    parallelogram_base = 10.0
    parallelogram_height = 5.0
    trapezoid_base = 8.0
    trapezoid_side_a = 6.0
    trapezoid_height = 4.0
    try:
        p_area, _ = calculate_area('parallelogram', parallelogram_base, parallelogram_height)
        t_area, _ = calculate_area('trapezoid', trapezoid_base, trapezoid_height, side_a=trapezoid_side_a)
        print(f'Parallelogram Area: {p_area}')
        print(f'Trapezoid Area: {t_area}')
        if p_area == t_area:
            print('The areas are equal.')
        else:
            print('The areas are not equal.')
    except ValueError as e:
        print(e)