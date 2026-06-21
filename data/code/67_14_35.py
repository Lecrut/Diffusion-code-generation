def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')
    return a + b

class SumComputer:

    def __init__(self, values=None):
        self.values = values or []

    def add_value(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Value to add must be an integer or floating-point number.')
        self.values.append(value)

    def compute_total(self):
        return sum(self.values)
if __name__ == '__main__':
    result1 = add(5, 3)
    print(result1)
    result2 = add(2.5, 4.7)
    print(result2)
    computer = SumComputer()
    computer.add_value(5)
    computer.add_value(3)
    print(computer.compute_total())
    computer.add_value(2.5)
    computer.add_value(4.7)
    print(computer.compute_total())