import math

class Square:
    @staticmethod
    def find_side_length(area):
        return math.sqrt(area)

if __name__ == '__main__':
    sample_areas = [25.0, 36.0, 49.0, 64.0]
    for area in sample_areas:
        side_length = Square.find_side_length(area)
        print(f'Area: {area}, Side Length: {side_length}')