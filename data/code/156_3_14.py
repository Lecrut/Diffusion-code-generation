class FloatList:
    def __init__(self, values):
        if not isinstance(values, list) or len(values) == 0:
            raise ValueError("Input must be a non-empty list of floats")
        self.values = values
    
    def mean(self):
        return sum(self.values) / len(self.values)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    calculator = FloatList(sample_values)
    print(calculator.mean())