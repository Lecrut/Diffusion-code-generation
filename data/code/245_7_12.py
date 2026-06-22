import math

class AreaComparer:
    @staticmethod
    def calculate_ellipse_area(semi_major_axis, semi_minor_axis):
        return math.pi * semi_major_axis * semi_minor_axis
    
    @staticmethod
    def calculate_rectangle_area(side_length):
        return side_length ** 2
    
    @staticmethod
    def compare_areas(ellipse_params, rectangle_params):
        ellipse_area = AreaComparer.calculate_ellipse_area(*ellipse_params)
        rectangle_area = AreaComparer.calculate_rectangle_area(*rectangle_params)
        difference = abs(ellipse_area - rectangle_area)
        if difference == 0:
            print("The difference between the areas is zero.")
        else:
            print(f"The difference between the areas is: {difference}")
        return difference

if __name__ == '__main__':
    ellipse_data = (5, 10)
    rectangle_data = (4, 10)
    AreaComparer.compare_areas(ellipse_data, rectangle_data)