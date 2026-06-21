def calculate_area(length, width):
    return length * width

def find_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    length1, width1 = (5, 3)
    length2, width2 = (4, 6)
    area1 = calculate_area(length1, width1)
    area2 = calculate_area(length2, width2)
    difference = find_difference(area1, area2)
    print(difference)