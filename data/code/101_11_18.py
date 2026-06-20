from datetime import date

class WeekdayCalculator:
    DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    @staticmethod
    def determine_weekday(year, month, day) -> str:
        date_obj = date(year, month, day)
        return WeekdayCalculator.DAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    print(WeekdayCalculator.determine_weekday(2023, 10, 10))