from typing import List

def convert_to_milliliters(liters_list: List[float]) -> List[float]:
    return [l * 1000 for l in liters_list]

if __name__ == '__main__':
    result = convert_to_milliliters([1.5, 2.0, 0.5])
    print(result)