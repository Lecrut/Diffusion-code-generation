from typing import Union

def convert_distance(value: float, from_unit: str, to_unit: str) -> Union[float, None]:
    conversion_factors = {'km': {'m': 1000, 'mi': 0.621371, 'ft': 3280.84}, 'm': {'km': 0.001, 'mi': 0.000621371, 'ft': 3.28084}, 'mi': {'km': 1.60934, 'm': 1609.34, 'ft': 5280}, 'ft': {'km': 0.0003048, 'm': 0.3048, 'mi': 0.000189394}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        return None
    return value * conversion_factors[from_unit][to_unit]
if __name__ == '__main__':
    print(convert_distance(1, 'km', 'm'))
    print(convert_distance(5, 'mi', 'ft'))
    print(convert_distance(1000, 'm', 'km'))