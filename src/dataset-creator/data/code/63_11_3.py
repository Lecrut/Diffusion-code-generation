import sys
from datetime import date
class DateSubtractor:
    def calculate_anniversary(self, start_year: int, end_year: int) -> list[date]:
        anniversaries = []
        for year in range(start_year, end_year + 1):
            try:
                current_date = date(year, 12, 30)
                anniversaries.append(current_date)
            except ValueError:
                continue
        return anniversaries
    def calculate_birthdays(self, start_month_day: tuple[int, int], end_year: int) -> list[date]:
        if not isinstance(start_month_day, tuple):
            raise TypeError("start_month_day must be a tuple of (month, day)")
        try:
            current_date = date(end_year, start_month_day[0], start_month_day[1])
            return [current_date]
        except ValueError as e:
            print(f"Invalid date for {end_year}: {e}")
            return []
def process_large_list(start_years: list[int], end_years: list[int], month_days: tuple) -> None:
    results = {}
    if not start_years or not end_years:
        print("No valid year ranges provided.")
        return
    for i, (start_y, end_y) in enumerate(zip(start_years, end_years)):
        try:
            anniversaries = DateSubtractor().calculate_anniversary(start_y, end_y)
            if month_days and len(month_days) == 2:
                birthdays = [date(end_y, month_days[0], month_days[1])]
                results[f"Range_{start_y}_to_{end_y}"] = {
                    "anniversaries": anniversaries,
                    "birthdays": birthdays
                }
        except Exception as e:
            print(f"Error processing range {i}: {e}")
    if results:
        for key, data in results.items():
            print(f"{key} - Anniversaries count: {len(data['anniversaries'])}, Birthdays count: {len(data['birthdays'])}")
if __name__ == '__main__':
    sample_years = [2015, 2020]
    sample_end_years = [2030, 2040]
    birthday_tuple = (6, 18)
    process_large_list(sample_years, sample_end_years, birthday_tuple)