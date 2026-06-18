import datetime as dt
def format_datetime_to_text(d: dt.datetime) -> str:
    year = d.year
    month_num = d.month
    day = d.day
    month_names = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    return f"{month_names[month_num]} {day}, {year}"
if __name__ == '__main__':
    sample_date = dt.datetime(2023, 10, 5)
    result_text = format_datetime_to_text(sample_date)
    print(result_text)