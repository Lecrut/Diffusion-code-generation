from datetime import datetime

def sort_dates(date_strings):
    def validate_and_parse(date_str):
        if not isinstance(date_str, str):
            raise ValueError("Input must be a string")
        parts = date_str.split('/')
        if len(parts) != 3:
            raise ValueError(f"Invalid format: {date_str}")
        day_str, month_str, year_str = parts
        if not (day_str.isdigit() and month_str.isdigit() and year_str.isdigit()):
            raise ValueError(f"Non-numeric components in: {date_str}")
        day = int(day_str)
        month = int(month_str)
        year = int(year_str)
        if not (1 <= month <= 12):
            raise ValueError(f"Invalid month: {month}")
        if not (1 <= day <= 31):
            raise ValueError(f"Invalid day: {day}")
        if year < 1:
            raise ValueError(f"Invalid year: {year}")
        try:
            return datetime(year=year, month=month, day=day)
        except ValueError:
            raise ValueError(f"Date out of valid range: {date_str}")

    parsed = []
    for ds in date_strings:
        dt = validate_and_parse(ds)
        parsed.append((dt, ds))
    
    parsed.sort(key=lambda x: x[0])
    return [item[1] for item in parsed]

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)