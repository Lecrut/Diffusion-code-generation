from datetime import date
if __name__ == '__main__':
    today = date.today()
    print(f"Today's date: {today}")
    days_of_week = [0, 1, 2, 3, 4, 5, 6]
    for day in days_of_week:
        weekday_index = today.weekday() % 7
        if weekday_index == day:
            print(f"The day {day} is a weekday.")
        else:
            print(f"The day {day} is not a weekday.")