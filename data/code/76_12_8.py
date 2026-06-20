import datetime

def calculate_date_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date_str1, date_format)
        date2 = datetime.datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        return difference
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-02-28"
    try:
        difference = calculate_date_difference(date1_str, date2_str)
        print(f"Date 1: {date1_str}")
        print(f"Date 2: {date2_str}")
        print(f"The difference between the two dates is {difference} days.")
    except ValueError as e:
        print(e)