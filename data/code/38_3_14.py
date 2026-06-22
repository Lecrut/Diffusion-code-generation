def cone_volume(radius, height):
    return 1/3 * 3.141592653589793 * radius**2 * height

if __name__ == '__main__':
    r = 4
    h = 12
    print(cone_volume(r, h))