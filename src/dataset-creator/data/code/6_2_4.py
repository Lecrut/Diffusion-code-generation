import math
def compare_integers(a: int, b: int) -> bool:
    return a > b
def compare_floats(a: float, b: float) -> bool:
    if not (math.isinf(a) or math.isnan(a)):
        if not (math.isinf(b) or math.isnan(b)):
            return a > b
    if math.isposinf(a):
        return True
    elif math.isneginf(a):
        return False
def compare_strings(a: str, b: str) -> bool:
    return a > b
class ComparisonModule:
    def __init__(self):
        self.ints = []
        self.floats = []
        self.strings = []
    def add_int(self, value: int) -> None:
        self.ints.append(value)
    def add_float(self, value: float) -> None:
        self.floats.append(value)
    def add_string(self, value: str) -> None:
        self.strings.append(value)
if __name__ == '__main__':
    module = ComparisonModule()
    module.add_int(10)
    module.add_int(25)
    module.add_float(3.14)
    module.add_float(-9.87)
    module.add_string("apple")
    module.add_string("banana")
    print(f"Integer comparison (25 > 10): {compare_integers(module.ints[1], module.ints[0])}")
    print(f"Float comparison (-9.87 < 3.14, so 3.14 > -9.87 is True): {compare_floats(3.14, -9.87)}")
    print(f"String comparison ('banana' > 'apple'): {compare_strings(module.strings[1], module.strings[0])}")