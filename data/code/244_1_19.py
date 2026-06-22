def calculate_area():
    shapes = {
        'rectangle': {'width': 10, 'height': 6},
        'triangle': {'base': 8, 'height': 5}
    }
    
    rectangle_area = shapes['rectangle']['width'] * shapes['rectangle']['height']
    triangle_area = 0.5 * shapes['triangle']['base'] * shapes['triangle']['height']
    total_area = rectangle_area + triangle_area
    
    return total_area

if __name__ == '__main__':
    print(calculate_area())