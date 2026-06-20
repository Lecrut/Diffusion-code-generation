from datetime import date

def get_weekday(year: int, month: int, day: int) -> str:
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_names[date(year, month, day).weekday()]

if __name__ == '__main__':
    sample_date = date(2023, 10, 10)
    print(get_weekday(sample_date.year, sample_date.month, sample_date.day))