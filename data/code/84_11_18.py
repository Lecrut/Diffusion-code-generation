import datetime

class DateUtils:
    def calculate_day_of_year(self, year: int, month: int, day: int) -> int:
        return (datetime.datetime(year, month, day) - datetime.datetime(year, 1, 1)).days + 1

if __name__ == '__main__':
    date_utils = DateUtils()
    print(f"Day of year for (2024, 3, 15): {date_utils.calculate_day_of_year(2024, 3, 15)}")
    print(f"Day of year for (2000, 1, 1): {date_utils.calculate_day_of_year(2000, 1, 1)}")
    print(f"Day of year for (2023, 12, 31): {date_utils.calculate_day_of_year(2023, 12, 31)}")
    print(f"Day of year for (2024, 2, 29): {date_utils.calculate_day_of_year(2024, 2, 29)}")
    print(f"Day of year for (2023, 1, 1): {date_utils.calculate_day_of_year(2023, 1, 1)}")