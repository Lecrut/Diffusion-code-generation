from typing import Union

class NumericAdder:
    def add(self, num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        return num1 + num2

if __name__ == '__main__':
    adder = NumericAdder()
    a = 10
    b = 5.5
    result = adder.add(a, b)
    print(f"The sum of {a} and {b} is {result}")
    
    x = -3
    y = 7
    result2 = adder.add(x, y)
    print(f"The sum of {x} and {y} is {result2}")