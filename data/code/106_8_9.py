import datetime
YEAR_DIFFERENCE_FACTOR = 365.2425

def calculate_year_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.datetime.strptime(date_str1, date_format)
    date2 = datetime.datetime.strptime(date_str2, date_format)
    time_diff = abs((date2 - date1).days)
    year_diff = time_diff / YEAR_DIFFERENCE_FACTOR
    return int(year_diff)
if __name__ == '__main__':
    date1 = '2000-01-01'
    date2 = '2023-04-15'
    difference = calculate_year_difference(date1, date2)
    print(difference)