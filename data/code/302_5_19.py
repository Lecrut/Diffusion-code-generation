class Year:
    def __init__(self, year):
        self.year = year

    def is_leap(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def total_days(self):
        if self.is_leap():
            return 366
        else:
            return 365

if __name__ == '__main__':
    year_2023 = Year(2023)
    print(year_2023.total_days())
    year_2024 = Year(2024)
    print(year_2024.total_days())