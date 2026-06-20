from datetime import date

def determine_weekday(year: int, month: int, day: int) -> str:
    try:
        date_obj = date(year, month, day)
        weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekday_names[date_obj.weekday()]
    except ValueError as e:
        return f"Invalid date: {e}"

if __name__ == '__main__':
    print(determine_weekday(2023, 10, 10))