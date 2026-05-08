from datetime import date
if __name__ == '__main__':
    today = date.today()
    print(f"Today's date: {today}")
    weekday_value = today.weekday()
    print(f"Weekday value (0=Monday, 6=Sunday): {weekday_value}")
    if weekday_value == 0:
        print("It is a Monday.")
    elif weekday_value == 6:
        print("It is a Sunday.")
    else:
        print("It is a weekday.")