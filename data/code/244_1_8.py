def calculate_area():
    rectangle_width = 10
    rectangle_height = 6
    triangle_base = 8
    triangle_height = 5
    
    rectangle_area = rectangle_width * rectangle_height
    triangle_area = 0.5 * triangle_base * triangle_height
    
    total_area = rectangle_area + triangle_area
    return total_area

if __name__ == '__main__':
    print(calculate_area())