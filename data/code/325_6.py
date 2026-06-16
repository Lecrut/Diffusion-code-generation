if __name__ == '__main__':
    length1 = 10
    width1 = 5
    length2 = 8
    width2 = 6
    area1 = length1 * width1
    area2 = length2 * width2
    if area1 > area2:
        print(f"Rectangle 1 has the larger area. Area 1: {area1}, Area 2: {area2}")
    elif area2 > area1:
        print(f"Rectangle 2 has the larger area. Area 1: {area1}, Area 2: {area2}")
    else:
        print(f"Both rectangles have the same area. Area: {area1}")