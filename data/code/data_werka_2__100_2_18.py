class AndGate:
    def __init__(self, name):
        self.name = name
        self.inputs = []

    def add_input(self, value):
        self.inputs.append(value)

    def evaluate(self):
        if len(self.inputs) != 3:
            raise ValueError(f"Expected 3 inputs, got {len(self.inputs)}")
        result = 1
        for val in self.inputs:
            result = result and val
        return result

    def check_validity(self, a, b, c):
        self.inputs = []
        self.add_input(a)
        self.add_input(b)
        self.add_input(c)
        computed = self.evaluate()
        return computed

if __name__ == '__main__':
    gate = AndGate("AND3")
    
    res1 = gate.check_validity(1, 1, 1)
    print(f"1 AND 1 AND 1 = {res1}")
    
    res2 = gate.check_validity(1, 0, 1)
    print(f"1 AND 0 AND 1 = {res2}")
    
    res3 = gate.check_validity(0, 0, 0)
    print(f"0 AND 0 AND 0 = {res3}")