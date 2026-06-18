from typing import Protocol, runtime_checkable
@runtime_checkable
class Summable(Protocol):
    def __add__(self, other: "Summable") -> float: ...
def aggregate_sum(a: Summable, b: Summable) -> float:
    return a + b
if __name__ == '__main__':
    class MyNumber(float):
        pass
    num1 = MyNumber(5.0)
    num2 = MyNumber(3.0)
    result = aggregate_sum(num1, num2)
    print(result)