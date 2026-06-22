def cone_volume(radius, height):
    return (1/3) * 3.141592653589793 * radius * radius * height

if __name__ == '__main__':
    r = 8
    h = 11
    result = cone_volume(r, h)
    print(f"{result:.2f}")