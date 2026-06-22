class FindTheMiddleValueAmongThreeProcessor:
    def __init__(self):
        self.values = []

    def add_value(self, value):
        self.values.append(value)

    def calculate_middle(self):
        if len(self.values) != 3:
            raise ValueError("Exactly three values are required to find the middle.")
        sorted_values = sorted(self.values)
        return sorted_values[1]

if __name__ == '__main__':
    processor = FindTheMiddleValueAmongThreeProcessor()
    processor.add_value(7)
    processor.add_value(4)
    processor.add_value(9)
    print(processor.calculate_middle())