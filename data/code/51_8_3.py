class GeometryUtils:
    @staticmethod
    def calculate_perimeter(side_a, side_b, side_c):
        return side_a + side_b + side_c
if __name__ == '__main__':
    a = 5
    b = 10
    c = 15
    perimeter = GeometryUtils.calculate_perimeter(a, b, c)
    print(perimeter)