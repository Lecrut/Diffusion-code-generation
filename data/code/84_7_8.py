class DayOfYearCalculator:
    EPOCH = 0

    @staticmethod
    def day_of_year(days_passed):
        return (days_passed - DayOfYearCalculator.EPOCH) % 365 + 1

if __name__ == '__main__':
    calculator = DayOfYearCalculator()
    print(calculator.day_of_year(0))
    print(calculator.day_of_year(364))
    print(calculator.day_of_year(365))