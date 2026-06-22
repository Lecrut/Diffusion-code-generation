def compute_square_pyramid_area(side, slant):
    if not isinstance(side, (int, float)) or not isinstance(slant, (int, float)):
        raise TypeError("Arguments must be numeric")
    if side <= 0 or slant <= 0:
        raise ValueError("Dimensions must be positive")
    
    BASE_AREA_FACTOR = 1
    LATERAL_FACTOR = 2
    
    base_part = side ** 2
    lateral_part = LATERAL_FACTOR * side * slant
    total = base_part + lateral_part
    return round(total, 2)

if __name__ == '__main__':
    b = 12
    s = 15
    val = compute_square_pyramid_area(b, s)
    print(val)