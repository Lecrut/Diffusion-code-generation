class GeometryCalculator:
    SIDE_LENGTH = 10

    @staticmethod
    def square_of_side(length):
        return length ** 2

if __name__ == '__main__':
    side_value = GeometryCalculator.SIDE_LENGTH
    calculated_result = GeometryCalculator.square_of_side(side_value)
    print(calculated_result)