class Square:
    @staticmethod
    def area(side):
        return side * side

if __name__ == '__main__':
    sample_sides = [3, 5, 7]
    for side in sample_sides:
        print(f"Side Length: {side}, Area: {Square.area(side)}")