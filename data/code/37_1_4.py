class GeometryCalculator:
    @staticmethod
    def compute_area(base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        return base * height

if __name__ == '__main__':
    geom = GeometryCalculator()
    b = 7
    h = 3
    print(geom.compute_area(b, h))