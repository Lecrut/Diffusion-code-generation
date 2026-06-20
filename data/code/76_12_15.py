from datetime import datetime

def days_between_dates(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return abs((date2 - date1).days)
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-28"
    try:
        difference = days_between_dates(date1_str, date2_str)
        print(f"Date 1: {date1_str}")
        print(f"Date 2: {date2_str}")
        print(f"The difference between the two dates is {difference} days.")
    except ValueError as e:
        print(e)