LITERS_TO_ML_FACTOR = 1000
UNIT_MAP = {'liters': LITERS_TO_ML_FACTOR}

def convert_volume(volume: float) -> float:
    return volume * UNIT_MAP['liters']

if __name__ == '__main__':
    volume_in_liters = 2
    result = convert_volume(volume_in_liters)
    print(result)