def calculate_area(diag1, diag2):
    return 0.5 * diag1 * diag2

def calculate_area_sum():
    areas = {
        "rhombus1": (6, 8),
        "rhombus2": (10, 12)
    }
    
    area1 = calculate_area(*areas["rhombus1"])
    area2 = calculate_area(*areas["rhombus2"])
    
    return area1 + area2

if __name__ == '__main__':
    result = calculate_area_sum()
    print(result)