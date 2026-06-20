from datetime import datetime

def days_between_dates(date1, date2):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = abs(a - b)
    return delta.days

if __name__ == '__main__':
    sample_date1 = "2023-04-01"
    sample_date2 = "2023-04-15"
    print(days_between_dates(sample_date1, sample_date2))