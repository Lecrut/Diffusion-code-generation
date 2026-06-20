from datetime import datetime

def contains_weekdays(date_strings):
    return any(datetime.strptime(date_str, '%Y-%m-%d').weekday() < 5 for date_str in date_strings)

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2023-10-02', '2023-10-06']
    print(contains_weekdays(sample_dates))