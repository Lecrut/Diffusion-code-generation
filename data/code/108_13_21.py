from datetime import date

class DayCalculator:
    def __init__(self, year: int, month: int, day: int) -> None:
        self._date_obj = date(year, month, day)

    def get_numeric_day(self) -> int:
        return self._date_obj.day

    def get_month_name(self) -> str:
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return months[self._date_obj.month - 1]

if __name__ == '__main__':
    calc = DayCalculator(2024, 10, 10)
    print(calc.get_numeric_day())
    print(calc.get_month_name())