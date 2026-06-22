from datetime import date

class YearSpanCalculator:
    START_MONTH = 1
    START_DAY = 1
    END_MONTH = 12
    END_DAY = 31

    @staticmethod
    def create_start_date(year):
        return date(year, YearSpanCalculator.START_MONTH, YearSpanCalculator.START_DAY)

    @staticmethod
    def create_end_date(year):
        return date(year, YearSpanCalculator.END_MONTH, YearSpanCalculator.END_DAY)

    def calculate_days(self, year):
        start = self.create_start_date(year)
        end = self.create_end_date(year)
        delta = end - start
        return delta.days

if __name__ == '__main__':
    calculator = YearSpanCalculator()
    target_year = 2023
    days = calculator.calculate_days(target_year)
    print(days)