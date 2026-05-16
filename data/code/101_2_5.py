from datetime import date
class DateConverter:
    def get_day_of_week(self, date_obj: date) -> int:
        return date_obj.weekday()
if __name__ == '__main__':
    converter = DateConverter()
    date1 = date(2023, 10, 23)
    day1 = converter.get_day_of_week(date1)
    print(f"Date: {date1}, Day of the week (Monday=0): {day1}")
    date2 = date(2024, 1, 1)
    day2 = converter.get_day_of_week(date2)
    print(f"Date: {date2}, Day of the week (Monday=0): {day2}")
    date3 = date(2025, 12, 31)
    day3 = converter.get_day_of_week(date3)
    print(f"Date: {date3}, Day of the week (Monday=0): {day3}")