def square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_side = 7.5
    area_result = square_area(sample_side)
    print(f"The side length of the square is: {sample_side}")
    print(f"The area of the square is: {area_result}")