from typing import Union

class NumericAdder:
    def sum_two_values(self, value1: Union[int, float], value2: Union[int, float]) -> Union[int, float]:
        return value1 + value2

if __name__ == '__main__':
    adder = NumericAdder()
    a = 10
    b = 5.5
    result = adder.sum_two_values(a, b)
    print(f"The sum of {a} and {b} is {result}")
    x = -3
    y = 7
    result2 = adder.sum_two_values(x, y)
    print(f"The sum of {x} and {y} is {result2}")