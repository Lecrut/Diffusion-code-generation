from typing import Protocol, runtime_checkable
@runtime_checkable
class Summable(Protocol):
    def __add__(self, other: "Summable") -> float: ...
def aggregate_sum(a: Summable, b: Summable) -> float:
    return a + b
if __name__ == '__main__':
    class MyInt(int):
        pass
    obj1 = MyInt(50)
    obj2 = MyInt(30)
    result = aggregate_sum(obj1, obj2)
    print(result)