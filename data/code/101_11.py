from datetime import date
def determine_weekday(date_obj: date) -> str:
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_names[date_obj.weekday()]
if __name__ == '__main__':
    date1 = date(2023, 10, 25)
    date2 = date(2024, 1, 1)
    date3 = date(2023, 12, 25)
    print(determine_weekday(date1))
    print(determine_weekday(date2))
    print(determine_weekday(date3))