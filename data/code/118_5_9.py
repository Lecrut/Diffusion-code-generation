from typing import Union

class Multiplier:
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b

if __name__ == '__main__':
    multiplier = Multiplier()
    result1 = multiplier.multiply(5, 10)
    print(result1)
    result2 = multiplier.multiply(3, 4.5)
    print(result2)