def compute_surface_area():
    l, w, h = 4, 6, 8
    return 2 * (l * w + l * h + w * h)

if __name__ == '__main__':
    print(compute_surface_area())