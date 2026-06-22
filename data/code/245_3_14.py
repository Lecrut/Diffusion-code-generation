def check_areas(width1, height1, width2, height2):
    return width1 * height1 == width2 * height2

if __name__ == '__main__':
    print(check_areas(4, 5, 20, 1))