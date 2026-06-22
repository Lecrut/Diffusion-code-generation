class PairAveragesCalculator:
    def __init__(self):
        self.first_sum = 0
        self.second_sum = 0
        self.count = 0

    @staticmethod
    def calculate(pairs):
        if not pairs:
            return {"first_average": None, "second_average": None}
        
        calculator = PairAveragesCalculator()
        for first, second in pairs:
            calculator.add_pair(first, second)
        return {"first_average": calculator.first_sum / calculator.count, "second_average": calculator.second_sum / calculator.count}

    def add_pair(self, first, second):
        self.first_sum += first
        self.second_sum += second
        self.count += 1

if __name__ == '__main__':
    sample_data = [(10, 20), (30, 40), (50, 60)]
    result = PairAveragesCalculator.calculate(sample_data)
    print(result)