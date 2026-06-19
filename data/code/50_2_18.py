def calculate_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    area1 = 50
    area2 = 30
    difference = calculate_difference(area1, area2)
    print(difference)