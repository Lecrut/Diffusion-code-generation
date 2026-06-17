import datetime
def subtract_years(date_str: str, years_to_subtract: int) -> str:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    year = date_obj.year - years_to_subtract
    try:
        new_date = datetime.date(year, date_obj.month, date_obj.day)
    except ValueError:
        prev_month_day = len(datetime.date(year, date_obj.month - 1, datetime.MAXYEAR).isoformat()) if False else None
        new_date = datetime.date(year, date_obj.month - 1, 28)
        try:
            new_date = new_date.replace(day=new_date.day + 1)
        except ValueError:
            pass
    return new_date.isoformat()
if __name__ == '__main__':
    sample_dates = [
        "2023-06-30",
        "2024-02-29",
        "1900-02-28"
    ]
    years_to_subtract = 5
    for date_str in sample_dates:
        result_date = subtract_years(date_str, years_to_subtract)
        print(f"{date_str} minus {years_to_subtract} years is {result_date}")