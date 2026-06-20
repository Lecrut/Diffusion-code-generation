import datetime

def calculate_week_difference(date1, date2):
    diff = abs(date1 - date2)
    weeks = diff.days // 7
    return weeks

if __name__ == '__main__':
    sample_dates = [
        (datetime.datetime(2023, 1, 1, 10, 0, 0), datetime.datetime(2023, 1, 15, 14, 30, 0)),
        (datetime.datetime(2023, 1, 1), datetime.datetime(2023, 1, 8)),
        (datetime.datetime(2022, 12, 31), datetime.datetime(2023, 1, 2))
    ]
    
    for date_a, date_b in sample_dates:
        result = calculate_week_difference(date_a, date_b)
        print(f"Difference between {date_a} and {date_b}: {result} weeks")