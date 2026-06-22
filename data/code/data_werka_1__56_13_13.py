def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    side_length = 5
    rectangle_length = 8
    rectangle_width = 6
    
    square_area = calculate_area(side_length, side_length)
    square_perimeter = calculate_perimeter(side_length, side_length)
    
    rectangle_area = calculate_area(rectangle_length, rectangle_width)
    rectangle_perimeter = calculate_perimeter(rectangle_length, rectangle_width)
    
    comparison = {
        'square': {
            'area': square_area,
            'perimeter': square_perimeter
        },
        'rectangle': {
            'area': rectangle_area,
            'perimeter': rectangle_perimeter
        }
    }
    
    print(comparison)