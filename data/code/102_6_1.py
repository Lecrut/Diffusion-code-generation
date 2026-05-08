from datetime import date
if __name__ == '__main__':
    today = date.today()
    print(f"Today's date: {today}")
    weekday_value = today.weekday()
    print(f"Weekday value (0=Monday, 6=Sunday): {weekday_value}")
    if weekday_value == 0:
        print("It is a Monday.")
    elif weekday_value == 1:
        print("It is a Tuesday.")
    elif weekday_value == 2:
        print("It is a Wednesday.")
    elif weekday_value == 3:
        print("It is a Thursday.")
    elif weekday_value == 4:
        print("It is a Friday.")
    elif weekday_value == 5:
        print("It is a Saturday.")
    else:
        print("It is a Sunday.")