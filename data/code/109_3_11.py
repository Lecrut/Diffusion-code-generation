from datetime import date

class MonthCalculator:
    @staticmethod
    def days_left_in_month():
        today = date.today()
        _, num_days = calendar.monthrange(today.year, today.month)
        return num_days - today.day

if __name__ == '__main__':
    print(MonthCalculator.days_left_in_month())