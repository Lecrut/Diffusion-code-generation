import math
def compare_integers(a: int, b: int) -> bool:
    return a > b
def compare_floats(a: float, b: float) -> bool:
    if not (math.isinf(a) or math.isinf(b)):
        return a > b
    elif math.isnan(a):
        return False
    else:
        return True
def compare_strings(a: str, b: str) -> bool:
    return a > b
class ComparisonModule:
    def __init__(self):
        self.ints = []
        self.floats = []
        self.strings = []
    def add_int(self, val: int):
        self.ints.append(val)
    def add_float(self, val: float):
        self.floats.append(val)
    def add_string(self, val: str):
        self.strings.append(val)
    def get_all_values(self):
        return {
            'integers': [x for x in self.ints if isinstance(x, int)],
            'floats': [x for x in self.floats if isinstance(x, float)],
            'strings': [x for x in self.strings if isinstance(x, str)]
        }
if __name__ == '__main__':
    module = ComparisonModule()
    sample_integers = [10, 5, -3]
    sample_floats = [2.718, 9.42, float('inf'), float('-inf')]
    sample_strings = ["zebra", "apple", "banana"]
    module.add_int(10)
    module.add_int(-5)
    for val in sample_integers:
        module.ints.append(val)
    for val in sample_floats:
        if isinstance(val, float):
            module.floats.append(val)
    for val in sample_strings:
        module.strings.append(val)
    data = module.get_all_values()
    print("Integers:", data['integers'])
    print("Floats:", data['floats'])
    print("Strings:", data['strings'])