from datetime import datetime

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        parts = date_str.split('/')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format: {date_str}")
        day, month, year = parts
        try:
            day_int = int(day)
            month_int = int(month)
            year_int = int(year)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
        try:
            dt = datetime(year=year_int, month=month_int, day=day_int)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
        parsed_dates.append(dt)
    
    sorted_dates = sorted(zip(parsed_dates, date_strings))
    sorted_date_strings = [date_str for _, date_str in sorted_dates]
    return sorted_date_strings

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/03/2023', '31/12/2022']
    result = sort_dates(sample_dates)
    print(result)