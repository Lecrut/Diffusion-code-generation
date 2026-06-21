MAX_BASE = 1000
MAX_HEIGHT = 1000

def calculate_triangle_area(base: float, height: float) -> float:
    if base <= 0 or base > MAX_BASE:
        raise ValueError(f"Base must be a positive number and less than or equal to {MAX_BASE}.")
    if height <= 0 or height > MAX_HEIGHT:
        raise ValueError(f"Height must be a positive number and less than or equal to {MAX_HEIGHT}.")
    
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 15
    sample_height = 6
    try:
        area = calculate_triangle_area(sample_base, sample_height)
        print(f"The area of the triangle is: {area}")
    except ValueError as e:
        print(e)