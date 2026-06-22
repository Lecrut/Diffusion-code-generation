AREA_UNITS = {
    "width": 0,
    "height": 1
}

def get_rectangle_area(side_a, side_b):
    return side_a * side_b

if __name__ == '__main__':
    base = 15
    altitude = 8
    computed_value = get_rectangle_area(base, altitude)
    print(computed_value)