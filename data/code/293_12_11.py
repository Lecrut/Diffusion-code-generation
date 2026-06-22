from typing import Union

def convert_distance(value: float, from_unit: str, to_unit: str) -> Union[float, None]:
    conversion_factors = {'km': 1000, 'm': 1, 'mi': 1609.34, 'ft': 3280.84}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return None
    meters = value * conversion_factors[from_unit]
    return meters / conversion_factors[to_unit]
if __name__ == '__main__':
    print(convert_distance(1, 'km', 'm'))
    print(convert_distance(5, 'mi', 'ft'))