class RangeCalculator:
    def __init__(self, sequence):
        self.sequence = sequence

    def calculate_range(self):
        if not self.sequence:
            return None
        current_min = current_max = self.sequence[0]
        for x in self.sequence[1:]:
            if x < current_min:
                current_min = x
            elif x > current_max:
                current_max = x
        return current_max - current_min

if __name__ == '__main__':
    calculator = RangeCalculator([10, 5, 20, 3, 15])
    print(calculator.calculate_range())