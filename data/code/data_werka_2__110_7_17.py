from datetime import datetime

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format: {date_str}")
        month, day, year = parts
        if not (month.isdigit() and day.isdigit() and year.isdigit()):
            raise ValueError(f"Invalid date format: {date_str}")
        month_int = int(month)
        day_int = int(day)
        year_int = int(year)
        if not (1 <= month_int <= 12):
            raise ValueError(f"Invalid month: {month_int}")
        if not (1 <= day_int <= 31):
            raise ValueError(f"Invalid day: {day_int}")
        if len(year) != 4:
            raise ValueError(f"Invalid year: {year}")
        try:
            dt = datetime(year_int, month_int, day_int)
        except ValueError:
            raise ValueError(f"Invalid date: {date_str}")
        parsed_dates.append((dt, date_str))
    
    parsed_dates.sort(key=lambda x: x[0])
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    dates = ['12-31-2023', '01-01-2023', '02-15-2023', '01-01-2022']
    sorted_dates = sort_dates(dates)
    print(sorted_dates)