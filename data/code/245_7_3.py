import math
def calculate_area_difference(circle_params, square_params):
    radius = circle_params[0]
    side = square_params[0]
    circle_area = math.pi * radius**2
    square_area = side**2
    difference = abs(circle_area - square_area)
    if difference == 0:
        print("The difference between the areas is zero.")
    return difference
if __name__ == '__main__':
    circle_params = (5, 10)
    square_params = (4, 10)
    result = calculate_area_difference(circle_params, square_params)
    print(f"The difference between the areas is: {result}")