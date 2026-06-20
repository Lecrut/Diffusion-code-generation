from datetime import date

class DateFormatter:
    def __init__(self, year: int, month: int, day: int):
        self.date_obj = date(year, month, day)

    def format_date(self) -> str:
        return f"{self.date_obj.day} {self.date_obj.strftime('%B')} {self.date_obj.year}"

if __name__ == '__main__':
    formatter = DateFormatter(2022, 11, 11)
    formatted_date = formatter.format_date()
    print(formatted_date)