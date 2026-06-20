from datetime import datetime

def dates_in_same_week(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    return date1.isocalendar()[1] == date2.isocalendar()[1]
if __name__ == '__main__':
    print(dates_in_same_week('2023-10-01', '2023-10-07'))
    print(dates_in_same_week('2023-10-01', '2023-10-08'))