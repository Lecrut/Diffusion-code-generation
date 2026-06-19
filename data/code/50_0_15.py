def calculate_area_difference(area1, area2):
    def abs_diff(a, b):
        return abs(a - b)
    
    areas = {
        'area1': area1,
        'area2': area2
    }
    
    return abs_diff(areas['area1'], areas['area2'])

if __name__ == '__main__':
    first_area_value = 100
    second_area_value = 75
    difference = calculate_area_difference(first_area_value, second_area_value)
    print(difference)