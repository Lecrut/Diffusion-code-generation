from datetime import date

def determine_weekday(year: int, month: int, day: int) -> str:
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    date_obj = date(year, month, day)
    return weekday_names[date_obj.weekday()]

if __name__ == '__main__':
    year_sample = 2023
    month_sample = 10
    day_sample = 10
    print(determine_weekday(year_sample, month_sample, day_sample))