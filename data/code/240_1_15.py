def compute_square_area(side_length):
    area = side_length * side_length
    return area

if __name__ == '__main__':
    side_length_1 = 8
    computed_area_1 = compute_square_area(side_length_1)
    print(f"The area of a square with side {side_length_1} is: {computed_area_1}")
    
    side_length_2 = 15
    computed_area_2 = compute_square_area(side_length_2)
    print(f"The area of a square with side {side_length_2} is: {computed_area_2}")