from datetime import date
if __name__ == '__main__':
    today = date.today()
    print(f"Today's date: {today}")
    weekday_today = today.weekday()
    print(f"Today's weekday (0=Monday, 6=Sunday): {weekday_today}")
    if weekday_today < 5:
        print("It is a weekday.")
    else:
        print("It is a weekend day.")
    specific_date = date(2023, 10, 27)
    print(f"\nDate: {specific_date}")
    weekday_specific = specific_date.weekday()
    print(f"Weekday for {specific_date}: {weekday_specific}")
    if weekday_specific < 5:
        print("Specific date is a weekday.")
    else:
        print("Specific date is a weekend day.")