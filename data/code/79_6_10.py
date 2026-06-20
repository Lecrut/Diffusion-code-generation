from datetime import date, timedelta

def next_month(date_obj):
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    
    if month == 12:
        new_year = year + 1
        new_month = 1
    else:
        new_year = year
        new_month = month + 1
    
    try:
        return date(new_year, new_month, day)
    except ValueError:
        if month in [4, 6, 9, 11] and day == 30:
            return date(new_year, new_month, 29)
        elif month == 2 and day == 29:
            return date(new_year, new_month, 28)
        else:
            raise

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    print(next_month(sample_date))