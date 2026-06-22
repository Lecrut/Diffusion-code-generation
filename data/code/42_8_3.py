import math

def ellipse_area():
    major_axis = 10
    minor_axis = 5
    radius_a = major_axis / 2
    radius_b = minor_axis / 2
    area = math.pi * radius_a * radius_b
    return area

if __name__ == '__main__':
    result = ellipse_area()
    print(result)