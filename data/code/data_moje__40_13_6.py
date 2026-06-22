class BoxSurfaceCalculator:
    DIMENSIONS = (4, 6, 8)

    @staticmethod
    def calculate():
        l, w, h = BoxSurfaceCalculator.DIMENSIONS
        return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    print(BoxSurfaceCalculator.calculate())