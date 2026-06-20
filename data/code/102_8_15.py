from datetime import datetime

class DateChecker:
    WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    @staticmethod
    def is_weekday(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.weekday() < 5
    
    @staticmethod
    def get_day_of_week(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return DateChecker.WEEKDAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    date1 = "2023-10-25"
    print(f"Date: {date1}, Day of the week: {DateChecker.get_day_of_week(date1)}, Is weekday: {DateChecker.is_weekday(date1)}")
    
    date2 = "2023-10-28"
    print(f"Date: {date2}, Day of the week: {DateChecker.get_day_of_week(date2)}, Is weekday: {DateChecker.is_weekday(date2)}")
    
    date3 = "2023-10-29"
    print(f"Date: {date3}, Day of the week: {DateChecker.get_day_of_week(date3)}, Is weekday: {DateChecker.is_weekday(date3)}")