from typing import Union

class Multiplier:
    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b

if __name__ == '__main__':
    result = Multiplier.multiply(5, 10)
    print(result)