import calendar
import datetime

def convert_date_format(date_str):
    try:
        parsed_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        month_index = parsed_date.month
        day = parsed_date.day
        year = parsed_date.year
        month_name = calendar.month_name[month_index]
        return f"{month_name} {day:02d}, {year}"
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}") from e

if __name__ == '__main__':
    sample_dates = ['2023-1-5', '2024-12-25', '2000-2-29']
    for d in sample_dates:
        result = convert_date_format(d)
        print(result)