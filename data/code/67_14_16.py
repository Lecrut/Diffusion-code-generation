from typing import List, Iterable

MILLILITERS_PER_LITER = 1000

def convert_volumes_to_milliliters(volumes: Iterable[float]) -> List[float]:
    return [volume * MILLILITERS_PER_LITER for volume in volumes]

if __name__ == '__main__':
    sample_volumes = [0.5, 1.25, 3.0, 7.5]
    result = convert_volumes_to_milliliters(sample_volumes)
    print(result)