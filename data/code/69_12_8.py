from typing import Union

def miles_to_feet_calc(miles: Union[int, float]) -> Union[int, float]:
    return miles * 5280

if __name__ == '__main__':
    result = miles_to_feet_calc(1)
    print(result)
    
    result = miles_to_feet_calc(2.5)
    print(result)