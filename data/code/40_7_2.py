def surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 3.0
    w = 4.0
    h = 5.0
    result = surface_area(l, w, h)
    print(result)