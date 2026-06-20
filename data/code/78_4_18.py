class MonthPathCalculator:
    MONTH_OFFSET = 12

    @staticmethod
    def calculate_shortest_path(month1, month2):
        return min(abs(month1 - month2), MonthPathCalculator.MONTH_OFFSET - abs(month1 - month2))

if __name__ == '__main__':
    calculator = MonthPathCalculator()
    print(calculator.calculate_shortest_path(12, 2))