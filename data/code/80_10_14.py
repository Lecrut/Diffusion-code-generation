import datetime

def compare_dates(date_str1, date_str2):
    return min(datetime.date.fromisoformat(date_str1), datetime.date.fromisoformat(date_str2))

if __name__ == '__main__':
    earlier_date = compare_dates('2023-04-01', '2023-05-01')
    print(earlier_date)