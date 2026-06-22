import operator

class ParallelogramArea:
    SHAPE = "parallelogram"

    @staticmethod
    def _multiply(a, b):
        return operator.mul(a, b)

    @classmethod
    def calculate_area(cls, base, height):
        return cls._multiply(base, height)

def calculate_area(base, height):
    return ParallelogramArea.calculate_area(base, height)

if __name__ == '__main__':
    b = 7
    h = 3
    area_result = calculate_area(b, h)
    print(area_result)