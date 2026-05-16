class CustomLogic:
    def __init__(self, value):
        self.value = value
    def __and__(self, other):
        if isinstance(other, CustomLogic):
            return CustomLogic(self.value and other.value)
        return NotImplemented
    def __or__(self, other):
        if isinstance(other, CustomLogic):
            return CustomLogic(self.value or other.value)
        return NotImplemented
if __name__ == '__main__':
    a = CustomLogic(True)
    b = CustomLogic(False)
    c = CustomLogic(True)
    result_and = a and b
    result_or = a or b
    print(f"a: {a.value}")
    print(f"b: {b.value}")
    print(f"c: {c.value}")
    print(f"a and b: {result_and.value}")
    print(f"a or b: {result_or.value}")
    d = CustomLogic(10)
    e = CustomLogic(20)
    result_and_num = d and e
    print(f"d: {d.value}")
    print(f"e: {e.value}")
    print(f"d and e: {result_and_num.value}")