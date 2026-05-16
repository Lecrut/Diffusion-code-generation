def find_area_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    test_area1 = 25.5
    test_area2 = 15.0
    result = find_area_difference(test_area1, test_area2)
    print(f"The difference between {test_area1} and {test_area2} is: {result}")
    test_area3 = 100
    test_area4 = 100
    result2 = find_area_difference(test_area3, test_area4)
    print(f"The difference between {test_area3} and {test_area4} is: {result2}")
    test_area5 = 3.14159
    test_area6 = 2.71828
    result3 = find_area_difference(test_area5, test_area6)
    print(f"The difference between {test_area5} and {test_area6} is: {result3}")