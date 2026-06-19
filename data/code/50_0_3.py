def calculate_area_difference(area1, area2):
    def absolute_difference(a, b):
        return abs(a - b)
    
    difference = absolute_difference(area1, area2)
    return difference

if __name__ == '__main__':
    first_area = 75
    second_area = 40
    result = calculate_area_difference(first_area, second_area)
    print(result)