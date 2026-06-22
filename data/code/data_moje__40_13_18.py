def compute_surface_area(l=4, w=6, h=8):
    return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    print(compute_surface_area())