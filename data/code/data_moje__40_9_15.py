def surface_area(l, w, h):
    return 2 * (l * w + w * h + l * h)

if __name__ == '__main__':
    l = 1.5
    w = 2.5
    h = 3.5
    result = surface_area(l, w, h)
    print(result)