from typing import Union

def miles_to_feet_calc(miles: Union[int, float]) -> float:
    return float(miles * 5280)

if __name__ == '__main__':
    sample_miles = 3.5
    result = miles_to_feet_calc(sample_miles)
    print(result)