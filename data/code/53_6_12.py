def calculate_square_area(side):
    return side * side

if __name__ == '__main__':
    side_length_1 = 4.0
    area_1 = calculate_square_area(side_length_1)
    print(f"Side Length: {side_length_1}, Area: {area_1}")
    
    side_length_2 = 6.5
    area_2 = calculate_square_area(side_length_2)
    print(f"Side Length: {side_length_2}, Area: {area_2}")
    
    side_length_3 = 0.0
    area_3 = calculate_square_area(side_length_3)
    print(f"Side Length: {side_length_3}, Area: {area_3}")