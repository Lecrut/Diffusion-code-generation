def is_square_area_greater():
    side_length_square = 5
    base_triangle = 4
    height_triangle = 3
    
    area_square = side_length_square ** 2
    area_triangle = 0.5 * base_triangle * height_triangle
    
    return area_square > area_triangle

if __name__ == '__main__':
    print(is_square_area_greater())