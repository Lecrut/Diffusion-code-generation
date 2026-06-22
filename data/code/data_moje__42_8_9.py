import math

def area_of_ellipse():
    major_axis = 10
    minor_axis = 5
    semi_major = major_axis / 2
    semi_minor = minor_axis / 2
    area = math.pi * semi_major * semi_minor
    return area

if __name__ == '__main__':
    result = area_of_ellipse()
    print(result)