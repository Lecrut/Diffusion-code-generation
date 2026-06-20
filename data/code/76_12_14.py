import datetime

def days_between_dates(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date_str1, date_format)
        date2 = datetime.datetime.strptime(date_str2, date_format)
        return abs((date2 - date1).days)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    try:
        result = days_between_dates('2023-01-01', '2023-01-31')
        print(f"The difference between the two dates is {result} days.")
    except ValueError as e:
        print(e)