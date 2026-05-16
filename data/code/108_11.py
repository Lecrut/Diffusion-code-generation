import datetime
def get_day_of_month(date_obj):
    try:
        return date_obj.day
    except AttributeError:
        return None
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 27)
    date2 = datetime.date(2024, 1, 1)
    date3 = datetime.date(2023, 12, 31)
    date_invalid = "not_a_date"
    print(f"Day of month for {date1}: {get_day_of_month(date1)}")
    print(f"Day of month for {date2}: {get_day_of_month(date2)}")
    print(f"Day of month for {date3}: {get_day_of_month(date3)}")
    print(f"Day of month for invalid input: {get_day_of_month(date_invalid)}")