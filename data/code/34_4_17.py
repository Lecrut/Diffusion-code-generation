def surface_area_of_cylinder():
    radius = 3.0
    height = 5.0
    pi = 3.141592653589793
    area = 2 * pi * radius * (radius + height)
    return area

if __name__ == '__main__':
    result = surface_area_of_cylinder()
    print(result)