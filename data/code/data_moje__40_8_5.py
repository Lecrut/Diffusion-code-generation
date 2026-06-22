def surface_area(l, w, h):
    return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    l, w, h = 3, 4, 5
    print(surface_area(l, w, h))