from typing import Union

def miles_to_feet_calc(miles: Union[int, float]) -> float:
    return miles * 5280

if __name__ == '__main__':
    sample_miles = 12.5
    result = miles_to_feet_calc(sample_miles)
    print(result)
    print(miles_to_feet_calc(0))
    print(miles_to_feet_calc(3))