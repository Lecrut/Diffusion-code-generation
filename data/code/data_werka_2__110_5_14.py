from datetime import datetime

def sort_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        parts = date_str.split('/')
        if len(parts) != 3:
            raise ValueError("Invalid date format")
        day, month, year = parts
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            raise ValueError("Invalid date components")
        day_int = int(day)
        month_int = int(month)
        year_int = int(year)
        if not (1 <= day_int <= 31 and 1 <= month_int <= 12 and year_int > 0):
            raise ValueError("Invalid date values")
        try:
            dt = datetime(year_int, month_int, day_int)
        except ValueError:
            raise ValueError(f"Invalid date: {date_str}")
        parsed_dates.append((dt, date_str))
    parsed_dates.sort(key=lambda x: x[0])
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    sample_dates = ['31/12/2023', '01/01/2023', '15/06/2022', '20/02/2023']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)