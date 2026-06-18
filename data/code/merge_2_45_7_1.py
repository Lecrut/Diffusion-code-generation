from typing import Protocol, runtime_checkable
@runtime_checkable
class Summable(Protocol):
    def __add__(self, other: "Summable") -> int | float: ...
def aggregate_sum(a: Summable, b: Summable) -> int | float:
    return a + b
if __name__ == '__main__':
    class MyInt(int):
        pass
    x = MyInt(10)
    y = MyInt(20)
    result = aggregate_sum(x, y)
    print(result)