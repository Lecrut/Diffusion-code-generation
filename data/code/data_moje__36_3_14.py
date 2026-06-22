def calculate_trapezoid_area(base1, base2, height):
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError("Base lengths and height must be positive numbers")
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    area1 = calculate_trapezoid_area(5, 7, 4)
    print(area1)
    
    area2 = calculate_trapezoid_area(3.5, 6.5, 2)
    print(area2)
    
    area3 = calculate_trapezoid_area(10, 10, 5)
    print(area3)