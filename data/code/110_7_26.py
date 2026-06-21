from datetime import datetime
import calendar

MONTH_NAMES = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April',
    '05': 'May', '06': 'June', '07': 'July', '08': 'August',
    '09': 'September', '10': 'October', '11': 'November', '12': 'December'
}

def sort_dates(date_strings):
    def parse_date(date_str):
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError(f"Invalid format: {date_str}")
        mm, dd, yyyy = parts
        if not (mm.isdigit() and dd.isdigit() and yyyy.isdigit()):
            raise ValueError(f"Invalid characters in: {date_str}")
        if len(yyyy) != 4:
            raise ValueError(f"Year must be 4 digits: {date_str}")
        
        month_int = int(mm)
        day_int = int(dd)
        year_int = int(yyyy)
        
        if month_int not in MONTH_NAMES:
            raise ValueError(f"Invalid month: {mm}")
        
        max_days = calendar.monthrange(year_int, month_int)[1]
        if day_int < 1 or day_int > max_days:
            raise ValueError(f"Invalid day {dd} for month {mm} in year {yyyy}")
            
        return datetime(year_int, month_int, day_int)

    sorted_dates = sorted(date_strings, key=parse_date)
    return sorted_dates

if __name__ == '__main__':
    dates = ['12-31-2023', '01-01-2023', '06-15-2022', '02-28-2023']
    result = sort_dates(dates)
    print(result)