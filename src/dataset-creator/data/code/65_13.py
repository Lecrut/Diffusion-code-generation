from typing import Protocol, TypeVar, Generic
T = TypeVar('T')
class MetricConverter(Protocol[T]):
    def to_imperial(self) -> 'ImperialResult': ...
class ImperialConverter(Protocol):
    from_metric: float
    @staticmethod
    def convert(feet_inches: tuple[int, int]) -> dict[str, float]:
        total_inches = feet_inches[0] * 12 + feet_inches[1]
        meters = round(total_inches * 0.0254, 3)
        centimeters = round(meters * 100, 2)
        return {
            "meters": meters,
            "centimeters": centimeters
        }
class ImperialResult(Generic[T]):
    def __init__(self, feet: int, inches: int):
        self.feet = feet
        self.inches = inches
    @property
    def total_inches(self) -> float:
        return self.feet * 12 + self.inches
class MetricConverterImpl(MetricConverter[float]):
    def __init__(self, meters: float):
        self.meters = round(meters, 3)
    def to_imperial(self) -> ImperialResult[int]:
        total_inches = int(round(self.meters / 0.0254))
        feet = total_inches // 12
        inches = total_inches % 12
        return ImperialResult(feet, inches)
class ImperialConverterImpl(ImperialConverter):
    def __init__(self, from_metric: float):
        self.from_metric = round(from_metric, 3)
def main():
    metric_value = 5.0
    converter1: MetricConverter[float] = MetricConverterImpl(metric_value)
    imperial_result: ImperialResult[int] = converter1.to_imperial()
    print(f"Metric Input: {metric_value} meters")
    print(f"Imperal Result - Feet: {imperial_result.feet}, Inches: {imperial_result.inches}")
    imperial_data = (3, 4)
    metric_output = ImperialConverterImpl.convert(imperial_data)
    print(f"Imperal Input - Feet: {imperial_data[0]}, Inches: {imperial_data[1]}")
    print(f"Metric Output - Meters: {metric_output['meters']}, Centimeters: {metric_output['centimeters']}")
if __name__ == '__main__':
    main()