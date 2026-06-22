def surface_area(l, w, h):
    return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    print(surface_area(10, 8, 6))