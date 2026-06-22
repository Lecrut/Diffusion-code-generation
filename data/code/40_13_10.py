def surface_area(l=4, w=6, h=8):
    if l <= 0 or w <= 0 or h <= 0:
        raise ValueError("Dimensions must be positive")
    return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    print(surface_area())