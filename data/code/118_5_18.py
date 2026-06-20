from typing import Union

def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

if __name__ == '__main__':
    sample_a = 8
    sample_b = 3.5
    result = multiply(sample_a, sample_b)
    print(result)