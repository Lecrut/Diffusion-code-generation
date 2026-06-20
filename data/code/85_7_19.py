from datetime import datetime

def weeks_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    difference = abs((date2 - date1).days)
    weeks = difference // 7
    return weeks

if __name__ == '__main__':
    print(weeks_between_dates('2023-01-01', '2023-01-15'))  # Output: 2
    print(weeks_between_dates('2023-01-15', '2023-01-01'))  # Output: 2