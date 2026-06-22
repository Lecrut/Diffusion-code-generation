import math

def calculate_side_length_from_height(height):
    return 2 * height / math.sqrt(3)

def calculate_perimeter(side_length):
    return 3 * side_length

if __name__ == '__main__':
    triangle_properties = {
        'height': 8.73,
        'side_length': None,
        'perimeter': None
    }
    
    triangle_properties['side_length'] = calculate_side_length_from_height(triangle_properties['height'])
    triangle_properties['perimeter'] = calculate_perimeter(triangle_properties['side_length'])
    
    print(f'Side Length: {triangle_properties["side_length"]}')
    print(f'Perimeter: {triangle_properties["perimeter"]}')