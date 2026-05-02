class GeometryUtils:
    @staticmethod
    def calculate_perimeter(side_a, side_b, side_c, side_d):
        return side_a + side_b + side_c + side_d
if __name__ == '__main__':
    a = 10
    b = 5
    c = 8
    d = 3
    perimeter = GeometryUtils.calculate_perimeter(a, b, c, d)
    print(perimeter)