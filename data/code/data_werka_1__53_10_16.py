def calculate_side_length(area):
    return area ** 0.5

if __name__ == '__main__':
    hard_coded_area = 25.0
    side_length = calculate_side_length(hard_coded_area)
    print(f"The side length of the square is: {side_length}")