class Shapes:
    def calculate_total_area(self, shape1_type, shape1_value, shape2_type, shape2_value):
        if shape1_type == "rectangle":
            area1 = shape1_value[0] * shape1_value[1]
        elif shape1_type == "circle":
            import math
            radius = shape1_value[0]
            area1 = math.pi * (radius ** 2)
        else:
            raise ValueError("Unsupported shape type for shape1")
        if shape2_type == "rectangle":
            area2 = shape2_value[0] * shape2_value[1]
        elif shape2_type == "circle":
            import math
            radius = shape2_value[0]
            area2 = math.pi * (radius ** 2)
        else:
            raise ValueError("Unsupported shape type for shape2")
        return area1 + area2
if __name__ == '__main__':
    shapes = Shapes()
    shape1_type = "rectangle"
    shape1_value = [4, 5]
    shape2_type = "circle"
    shape2_value = [3]
    total_area = shapes.calculate_total_area(shape1_type, shape1_value, shape2_type, shape2_value)
    print(total_area)