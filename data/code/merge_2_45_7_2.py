from typing import Protocol, runtime_checkable
@runtime_checkable
class Summable(Protocol):
    def __add__(self: "Summable", other: "Summable") -> int: ...
def aggregate_total(a: Summable, b: Summable) -> int:
    return a + b
if __name__ == '__main__':
    class MyInt(int):
        pass
    obj1 = MyInt(50)
    obj2 = MyInt(30)
    result = aggregate_total(obj1, obj2)
    print(result)