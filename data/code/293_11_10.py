import math

class ShapeCalculator:
    def calculate_area_circle(self, radius: float) -> dict:
        area_metric = math.pi * (radius ** 2)
        area_imperial = area_metric / 10.7639
        return {"metric": round(area_metric, 2), "imperial": round(area_imperial, 2)}

    def calculate_area_rectangle(self, length: float, width: float) -> dict:
        area_metric = length * width
        area_imperial = area_metric / 144
        return {"metric": round(area_metric, 2), "imperial": round(area_imperial, 2)}

    def calculate_area_triangle(self, base: float, height: float) -> dict:
        area_metric = (base * height) / 2
        area_imperial = area_metric / 144
        return {"metric": round(area_metric, 2), "imperial": round(area_imperial, 2)}

if __name__ == '__main__':
    calculator = ShapeCalculator()
    print(calculator.calculate_area_circle(5))
    print(calculator.calculate_area_rectangle(10, 20))
    print(calculator.calculate_area_triangle(7, 4))