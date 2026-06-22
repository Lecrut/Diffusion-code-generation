from datetime import date

class DateExtractor:
    def __init__(self, year: int, month: int, day: int):
        self.target_date = date(year, month, day)

    def get_day(self) -> int:
        return self.target_date.day

    def get_month(self) -> int:
        return self.target_date.month

    def get_year(self) -> int:
        return self.target_date.year

if __name__ == '__main__':
    extractor = DateExtractor(2024, 10, 10)
    print(extractor.get_day())
    print(extractor.get_month())
    print(extractor.get_year())