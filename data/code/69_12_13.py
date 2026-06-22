from typing import Union

def miles_to_feet_calc(miles: Union[int, float]) -> float:
    return float(miles) * 5280

if __name__ == '__main__':
    result = miles_to_feet_calc(2)
    print(result)