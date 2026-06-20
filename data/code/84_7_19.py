class DayOfYearCalculator:
    DAYS_PER_YEAR = 365

    def __init__(self, epoch):
        self.epoch = epoch

    @staticmethod
    def day_of_year(days_passed):
        return (days_passed % DayOfYearCalculator.DAYS_PER_YEAR) + 1

if __name__ == '__main__':
    calculator = DayOfYearCalculator(0)
    print(calculator.day_of_year(0))
    print(calculator.day_of_year(364))
    print(calculator.day_of_year(365))