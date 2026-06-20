from datetime import date

class DateWeekdayInfo:
    WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_day_info(dt: date) -> tuple[str, int]:
        day_index = dt.weekday()
        day_name = DateWeekdayInfo.WEEKDAY_NAMES[day_index]
        day_number = day_index + 1
        return (day_name, day_number)

if __name__ == '__main__':
    sample_date = date(2025, 3, 15)
    result = DateWeekdayInfo.get_day_info(sample_date)
    print(f"Date: {sample_date}, Day Name: {result[0]}, Day Number: {result[1]}")