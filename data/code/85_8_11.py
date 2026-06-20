import datetime

def date_difference_in_weeks(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        time_difference = abs((date1 - date2).days)
        difference_in_weeks = time_difference / 7
        return difference_in_weeks
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-29"
    result = date_difference_in_weeks(date1, date2)
    print(result)