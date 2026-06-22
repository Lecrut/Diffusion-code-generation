def area_circle(radius):
    return 3.14 * radius ** 2

def area_rectangle(length, width):
    return length * width

if __name__ == '__main__':
    circle_area = area_circle(5)
    rectangle_area = area_rectangle(4, 6)
    total_area = circle_area + rectangle_area
    print(total_area)