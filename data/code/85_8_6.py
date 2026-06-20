import datetime

def calculate_weeks_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date_obj1 = datetime.datetime.strptime(date_str1, date_format)
    date_obj2 = datetime.datetime.strptime(date_str2, date_format)
    time_delta = abs((date_obj1 - date_obj2).days)
    weeks_difference = time_delta / 7
    return weeks_difference

if __name__ == '__main__':
    sample_date1 = "2023-05-15"
    sample_date2 = "2023-06-25"
    result = calculate_weeks_difference(sample_date1, sample_date2)
    print(result)