import datetime
def format_date_string(date_string):
    try:
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        month = date_object.strftime("%m")
        day = date_object.strftime("%d")
        return f"{month}{day}"
    except ValueError:
        return "Invalid date format"
if __name__ == '__main__':
    date1 = "2023-10-05"
    date2 = "2024-01-31"
    date3 = "1999-12-01"
    print(format_date_string(date1))
    print(format_date_string(date2))
    print(format_date_string(date3))