import operator

class ParallelogramGeometry:
    multiplier = operator.mul

    @staticmethod
    def calculate_area(base, height):
        return ParallelogramGeometry.multiplier(base, height)

if __name__ == '__main__':
    base_val = 12.5
    height_val = 4.0
    print(ParallelogramGeometry.calculate_area(base_val, height_val))