def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    areas = {
        'room': 50.7,
        'garden': 35.4
    }
    difference = calculate_area_difference(areas['room'], areas['garden'])
    print(difference)