import datetime

def calculate_weeks_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(date_str1, date_format)
    date2 = datetime.datetime.strptime(date_str2, date_format)
    time_diff = abs((date1 - date2).days)
    weeks_diff = time_diff / 7
    return weeks_diff

if __name__ == '__main__':
    sample_date1 = "2023-02-01"
    sample_date2 = "2023-02-28"
    result = calculate_weeks_difference(sample_date1, sample_date2)
    print(result)