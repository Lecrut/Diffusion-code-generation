from typing import Protocol, Union
class MetricUnit(Protocol):
    value: float
    unit_name: str
class ImperialUnit(Protocol):
    feet: int
    inches: int
def convert_metric_to_imperial(metric_unit: MetricUnit) -> tuple[int, int]:
    meters = metric_unit.value * 3.28084
    total_inches = meters * 39.3701
    return (int(total_inches // 12), int(round((total_inches % 12))))
def convert_imperial_to_metric(feet: int, inches: int) -> float:
    total_feet = feet + (inches / 12)
    meters = total_feet * 0.3048
    return round(meters, 5)
if __name__ == '__main__':
    metric_input: MetricUnit = type('obj', (), {'value': 10.0, 'unit_name': 'm'})()
    feet_result, inches_result = convert_metric_to_imperial(metric_input)
    imperial_input: tuple[int, int] = (5, 9)
    meters_result = convert_imperial_to_metric(*imperial_input)
    print(f"Metric {metric_input.value} m -> Imperial {feet_result}' {inches_result}\"")
    print(f"Impreal {imperial_input[0]}' {imperial_input[1]}\" -> Metric {meters_result} m")