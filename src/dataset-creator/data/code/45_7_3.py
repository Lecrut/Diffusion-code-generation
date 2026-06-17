from typing import Protocol, Any
class Summable(Protocol):
    def total(self) -> int: ...
def aggregate_sum(a: Summable, b: Summable) -> int:
    return a.total() + b.total()
if __name__ == '__main__':
    class Item1(Summable):
        def total(self) -> int:
            return 5
    class Item2(Summable):
        def total(self) -> int:
            return 3
    result = aggregate_sum(Item1(), Item2())
    print(result)