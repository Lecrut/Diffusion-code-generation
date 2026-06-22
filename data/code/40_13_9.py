def surface_area(l=4, w=6, h=8):
    return 2 * (l*w + w*h + h*l)

if __name__ == '__main__':
    print(surface_area(4, 6, 8))