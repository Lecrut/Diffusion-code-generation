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
    d = CustomLogic(False)
    result_and_c = c and d
    print(f"c and d: {result_and_c.value}")