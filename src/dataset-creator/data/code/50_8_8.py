from typing import TypeVar, Union, overload
class SafeSum:
    @overload
    def calculate(self, a: int, b: int, c: int) -> int: ...
    @overload
    def calculate(self, a: float, b: float, c: float) -> float: ...
    @overload
    def calculate(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]: ...
    def calculate(self, a: int | float, b: int | float = 0.0, c: int | float = 0.0) -> Union[int, float]:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise TypeError("All arguments must be integers or floats.")
        return a + b + c
if __name__ == '__main__':
    result = SafeSum().calculate(10, 20.5, -3)
    print(result)