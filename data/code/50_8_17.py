def compute_area_difference(area1, area2):
    difference = abs(area1 - area2)
    return difference

if __name__ == '__main__':
    first_area = 75.3
    second_area = 48.9
    result = compute_area_difference(first_area, second_area)
    print(f"The absolute difference between {first_area} and {second_area} is: {result}")
    
    third_area = 200
    fourth_area = 150
    result2 = compute_area_difference(third_area, fourth_area)
    print(f"The absolute difference between {third_area} and {fourth_area} is: {result2}")
    
    fifth_area = 1.618
    sixth_area = 0.618
    result3 = compute_area_difference(fifth_area, sixth_area)
    print(f"The absolute difference between {fifth_area} and {sixth_area} is: {result3}")