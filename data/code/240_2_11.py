class Geometry:
    @staticmethod
    def square_area(side_length):
        return side_length * side_length

if __name__ == '__main__':
    sample_side = 10
    area = Geometry.square_area(sample_side)
    print(area)