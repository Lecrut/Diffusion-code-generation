from typing import Union

def miles_to_feet_calc(miles: Union[int, float]) -> float:
    feet_per_mile = 5280
    return miles * feet_per_mile

if __name__ == '__main__':
    sample_miles = 3.5
    result = miles_to_feet_calc(sample_miles)
    print(result)