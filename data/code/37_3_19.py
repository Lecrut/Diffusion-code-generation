class Parallelogram:
    _base: float = 12.5
    _height: float = 8.0

    @staticmethod
    def compute_area(base_val: float, height_val: float) -> float:
        return float(base_val * height_val)

if __name__ == '__main__':
    b = Parallelogram._base
    h = Parallelogram._height
    area_result = Parallelogram.compute_area(b, h)
    print(area_result)