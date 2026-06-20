from typing import Union

def subtract_values(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a - b

if __name__ == '__main__':
    first_number = 25
    second_number = 10
    result = subtract_values(first_number, second_number)
    print(result)