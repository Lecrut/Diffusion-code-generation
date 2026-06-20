import datetime

def format_date_string(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        month_name = date_obj.strftime("%B")
        day = date_obj.strftime("%d")
        year = date_obj.strftime("%Y")
        return f"{month_name} {day}, {year}"
    except ValueError:
        raise ValueError("Invalid date format")

if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "2024-01-31"
    date3 = "2022-12-01"
    
    try:
        print(format_date_string(date1))
        print(format_date_string(date2))
        print(format_date_string(date3))
    except ValueError as e:
        print(e)