from datetime import date

class DateProcessor:
    def __init__(self, year: int, month: int, day: int):
        self.date_obj = date(year, month, day)

    def get_day_of_month(self) -> int:
        return self.date_obj.day

if __name__ == '__main__':
    processor = DateProcessor(2024, 10, 10)
    print(processor.get_day_of_month())