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
    result_and_complex = a and c
    result_or_complex = a or c
    print(f"a: {a.value}, b: {b.value}, c: {c.value}")
    print(f"a and b: {result_and.value}")
    print(f"a or b: {result_or.value}")
    print(f"a and c: {result_and_complex.value}")
    print(f"a or c: {result_or_complex.value}")