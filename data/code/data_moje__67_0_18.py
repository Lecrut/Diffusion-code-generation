from typing import List, Union

def liters_to_milliliters(liters: List[Union[int, float]]) -> List[Union[int, float]]:
    return [liters_in_liter * 1000 for liters_in_liter in liters]

if __name__ == '__main__':
    sample_liters = [1.5, 2, 0.5]
    result = liters_to_milliliters(sample_liters)
    print(result)