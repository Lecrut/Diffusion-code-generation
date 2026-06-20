import math

def calculate_triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")
    
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The given sides do not form a valid triangle.")
    
    s = (a + b + c) / 2
    area_squared = s * (s - a) * (s - b) * (s - c)
    
    if area_squared < 0:
        raise ValueError("Numerical error resulted in a negative value under the square root.")
    
    return math.sqrt(area_squared)

if __name__ == '__main__':
    side_a = 3.0
    side_b = 4.0
    side_c = 5.0
    result = calculate_triangle_area(side_a, side_b, side_c)
    print(result)