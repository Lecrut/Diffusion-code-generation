CONST_METER_TO_FOOT = 3.28084

def meters_to_feet(value: float) -> float:
    return value * CONST_METER_TO_FOOT

if __name__ == '__main__':
    _METERS = 10
    print(meters_to_feet(_METERS))