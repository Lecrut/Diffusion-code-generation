from datetime import date
class DateConverter:
    def get_day_of_week(self, date_obj: date) -> int:
        return date_obj.weekday()
if __name__ == '__main__':
    converter = DateConverter()
    date1 = date(2023, 10, 2)
    day1 = converter.get_day_of_week(date1)
    print(f"Date: {date1}, Day of Week (Monday=0): {day1}")
    date2 = date(2023, 1, 1)
    day2 = converter.get_day_of_week(date2)
    print(f"Date: {date2}, Day of Week (Monday=0): {day2}")
    date3 = date(2024, 12, 25)
    day3 = converter.get_day_of_week(date3)
    print(f"Date: {date3}, Day of Week (Monday=0): {day3}")
    date4 = date(2025, 5, 15)
    day4 = converter.get_day_of_week(date4)
    print(f"Date: {date4}, Day of Week (Monday=0): {day4}")