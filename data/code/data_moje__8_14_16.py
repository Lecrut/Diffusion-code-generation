class AreaCalculator:
    def __init__(self, base_area: float) -> None:
        self.base_area = base_area

    def calculate_scaled_area(self, scale_factor: float) -> float:
        squared_factor = scale_factor * scale_factor
        return self.base_area * squared_factor

def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    calculator = AreaCalculator(base_area)
    return calculator.calculate_scaled_area(scale_factor)

if __name__ == '__main__':
    calc_instance = AreaCalculator(25.0)
    result1 = calc_instance.calculate_scaled_area(2.0)
    result2 = calc_instance.calculate_scaled_area(3.0)
    result3 = calculate_scaled_area(10.0, 4.0)
    print(result1)
    print(result2)
    print(result3)