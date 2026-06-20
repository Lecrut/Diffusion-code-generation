import datetime

def get_next_month(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        year = date_obj.year
        month = date_obj.month
        
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        
        return datetime.date(next_year, next_month, 1)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

if __name__ == '__main__':
    sample_date_str = "2023-12-15"
    try:
        next_date = get_next_month(sample_date_str)
        print(next_date.strftime("%Y-%m-%d"))
    except ValueError as e:
        print(e)