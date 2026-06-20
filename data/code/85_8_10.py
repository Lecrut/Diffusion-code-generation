import datetime

def date_difference_in_weeks(date1_str, date2_str):
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)
    time_difference = abs((date1 - date2).days)
    difference_in_weeks = round(time_difference / 7, 2)
    return difference_in_weeks

if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2023-01-29"
    result = date_difference_in_weeks(date_a, date_b)
    print(result)