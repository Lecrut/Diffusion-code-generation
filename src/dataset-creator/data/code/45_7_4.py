from typing import Protocol, runtime_checkable
@runtime_checkable
class Summable(Protocol):
    def __add__(self, other: "Summable") -> int | float: ...
def aggregate_total(obj1: Summable, obj2: Summable) -> int | float:
    return obj1 + obj2
if __name__ == '__main__':
    class ValueWrapper(Summable):
        def __init__(self, value: int | float):
            self.value = value
        def __add__(self, other: "ValueWrapper") -> int | float:
            return self.value + other.value
    val1 = ValueWrapper(10)
    val2 = ValueWrapper(25.5)
    result = aggregate_total(val1, val2)
    print(result)