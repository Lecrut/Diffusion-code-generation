def calculate_triangle_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError('Base and height must be numbers.')
    if base <= 0 or height <= 0:
        raise ValueError('Base and height must be positive numbers.')
    area = 0.5 * base * height
    return area
if __name__ == '__main__':
    try:
        sample_base = 12.5
        sample_height = 4.8
        triangle_area = calculate_triangle_area(sample_base, sample_height)
        print(f'The area of the triangle with base {sample_base} and height {sample_height} is: {triangle_area}')
    except (TypeError, ValueError) as e:
        print(e)