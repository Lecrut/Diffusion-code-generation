from typing import List, Union

def convert_to_milliliters(liters: List[Union[int, float]]) -> List[Union[int, float]]:
    return [l * 1000 for l in liters]

if __name__ == '__main__':
    sample_liters = [1.5, 2, 0.5]
    result = convert_to_milliliters(sample_liters)
    print(result)