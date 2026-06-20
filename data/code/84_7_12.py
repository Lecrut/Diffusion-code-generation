class DayOfYearCalculator:

    def __init__(self, epoch):
        self.epoch = epoch

    def day_of_year(self, days_passed):
        return (days_passed - self.epoch) % 365 + 1
if __name__ == '__main__':
    calculator = DayOfYearCalculator(0)
    print(calculator.day_of_year(0))
    print(calculator.day_of_year(364))
    print(calculator.day_of_year(365))
    print(calculator.day_of_year(729))