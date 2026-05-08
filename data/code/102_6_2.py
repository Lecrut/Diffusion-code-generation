from datetime import date
if __name__ == '__main__':
    today = date.today()
    print(f"Today's date: {today}")
    weekday_today = today.weekday()
    print(f"Today's weekday (0=Monday, 6=Sunday): {weekday_today}")
    if weekday_today == 0:
        print("Today is a Monday.")
    elif weekday_today == 1:
        print("Today is a Tuesday.")
    elif weekday_today == 2:
        print("Today is a Wednesday.")
    elif weekday_today == 3:
        print("Today is a Thursday.")
    elif weekday_today == 4:
        print("Today is a Friday.")
    elif weekday_today == 5:
        print("Today is a Saturday.")
    elif weekday_today == 6:
        print("Today is a Sunday.")
    else:
        print("This is an unexpected weekday value.")
    specific_date = date(2023, 10, 25)
    print(f"\nDate: {specific_date}")
    weekday_specific = specific_date.weekday()
    print(f"Weekday for {specific_date}: {weekday_specific}")
    if weekday_specific == 4:
        print("This date is a Friday.")
    else:
        print("This date is not a Friday.")