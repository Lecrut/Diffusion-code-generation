class GeometryCalculator:
    @staticmethod
    def calculate_parallelogram_area(base: float, height: float) -> float:
        return base * height

    @staticmethod
    def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
        return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    base_parallelogram = 5.0
    height_parallelogram = 3.0
    base1_trapezoid = 4.0
    base2_trapezoid = 6.0
    height_trapezoid = 2.0

    area_parallelogram = GeometryCalculator.calculate_parallelogram_area(base_parallelogram, height_parallelogram)
    area_trapezoid = GeometryCalculator.calculate_trapezoid_area(base1_trapezoid, base2_trapezoid, height_trapezoid)

    print(f"Parallelogram Area: {area_parallelogram}")
    print(f"Trapezoid Area: {area_trapezoid}")
    if area_parallelogram == area_trapezoid:
        print("The areas are equal.")
    else:
        print("The areas are not equal.")