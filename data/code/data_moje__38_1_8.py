def calculate_cone_volume(radius, height):
    return (1 / 3) * 3.141592653589793 * (radius ** 2) * height

if __name__ == '__main__':
    r = 5
    h = 10
    result = calculate_cone_volume(r, h)
    print(result)