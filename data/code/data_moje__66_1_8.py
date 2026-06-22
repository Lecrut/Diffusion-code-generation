KILOMETER_TO_METER_FACTOR = 1000

def convert_to_meters(kilometers: float) -> float:
    return kilometers * KILOMETER_TO_METER_FACTOR

if __name__ == '__main__':
    km_value = 5
    result = convert_to_meters(km_value)
    print(result)