def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

class Square:
    def __init__(self, area):
        self.area = area

    def side_length(self):
        return find_side_length(self.area)

if __name__ == '__main__':
    SMALL_AREA = 9
    MEDIUM_AREA = 25
    LARGE_AREA = 49

    areas_to_test = [SMALL_AREA, MEDIUM_AREA, LARGE_AREA]
    
    for area in areas_to_test:
        square = Square(area)
        print(f"The side length of a square with area {area} is {square.side_length()}")