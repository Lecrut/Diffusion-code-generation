from typing import Protocol, Union
class MetricUnit(Protocol):
    value: float
    def to_imperial(self) -> 'ImperialResult': ...
class ImperialUnit(Protocol):
    feet: int
    inches: int
    @classmethod
    def from_metric(cls, meters: float) -> 'Self': ...
def convert_to_feet_inches(meters: Union[float, MetricUnit]) -> tuple[int, int]:
    if isinstance(meters, (int, float)):
        total_inches = round((meters * 39.3701), -2)
        feet = total_inches // 12
        inches = total_inches % 12
        return feet, inches
    result: Union[tuple[int, int], 'ImperialUnit'] = meters.to_imperial()
    if isinstance(result, tuple):
        return result[0], result[1]
    else:
        return result.feet, result.inches
def convert_to_meters(feet_inches: Union[tuple[int, int], ImperialUnit]) -> float:
    total_inches = 0
    if isinstance(feet_inches, tuple):
        feet, inches = feet_inches
        total_inches = (feet * 12) + inches
    else:
        total_inches = (feet_inches.feet * 12) + feet_inches.inches
    meters = round((total_inches / 39.3701), -4)
    return meters
if __name__ == '__main__':
    sample_metric_value = 5.0
    result_feet, result_inches = convert_to_feet_inches(sample_metric_value)
    print(f"{result_feet} feet {result_inches} inches")
    imperial_sample: tuple[int, int] = (12, 6)
    converted_meters = convert_to_meters(imperial_sample)
    print(f"Converted to meters: {converted_meters}")