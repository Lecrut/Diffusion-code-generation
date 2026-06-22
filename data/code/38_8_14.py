def cone_volume(radius, height):
    return 3.14159265359 * radius * radius * height / 3

if __name__ == '__main__':
    r = 8
    h = 11
    result = cone_volume(r, h)
    print(f"{result:.2f}")