from datetime import datetime

class WeekdayChecker:
    WEEKDAY = range(5)
    
    @staticmethod
    def is_weekday(date_string: str) -> bool:
        try:
            date_obj = datetime.strptime(date_string, '%Y-%m-%d')
            return date_obj.weekday() in WeekdayChecker.WEEKDAY
        except ValueError:
            raise ValueError("Invalid Date Format")

if __name__ == '__main__':
    checker = WeekdayChecker()
    dates = ["2023-10-23", "2023-10-29", "2023-10-28", "2023-10-27", "2023-10-28", "2023-10-30"]
    for date in dates:
        print(f"{date}: {checker.is_weekday(date)}")