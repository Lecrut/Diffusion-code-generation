from datetime import date

class DayOfMonthCalculator:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.date_instance = date(year, month, day)

    def get_numeric_day(self) -> int:
        return self.date_instance.day

    def get_month_name(self) -> str:
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return months[self.date_instance.month - 1]

if __name__ == '__main__':
    calculator = DayOfMonthCalculator(2024, 10, 10)
    print(calculator.get_numeric_day())
    print(calculator.get_month_name())