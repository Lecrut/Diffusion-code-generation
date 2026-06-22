def surface_area(l, w, h):
    return 2 * (l * w + l * h + w * h)

if __name__ == '__main__':
    l = 10
    w = 8
    h = 6
    print(surface_area(l, w, h))