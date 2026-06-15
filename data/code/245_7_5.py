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
    square_params = (10, 10)
    result = calculate_area_difference(circle_params, square_params)
    print(f"Area difference: {result}")
    circle_params_2 = (3, 5)
    square_params_2 = (4, 4)
    result_2 = calculate_area_difference(circle_params_2, square_params_2)
    print(f"Area difference: {result_2}")