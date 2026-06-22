def calculate_rectangle_area(length, width):
    return length * width

if __name__ == '__main__':
    shape_params = {
        'rectangle': {'length': 5, 'width': 3}
    }
    
    area = calculate_rectangle_area(
        shape_params['rectangle']['length'],
        shape_params['rectangle']['width']
    )
    
    print(area)