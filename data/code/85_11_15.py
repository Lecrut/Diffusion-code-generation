import datetime

def calculate_week_difference(date1, date2):
    difference = abs(date2 - date1)
    weeks = difference.days // 7
    return weeks
if __name__ == '__main__':
    sample_date1 = datetime.date(2023, 4, 1)
    sample_date2 = datetime.date(2023, 4, 15)
    result1 = calculate_week_difference(sample_date1, sample_date2)
    print(result1)
    sample_date3 = datetime.date(2023, 10, 10)
    sample_date4 = datetime.date(2023, 10, 7)
    result2 = calculate_week_difference(sample_date3, sample_date4)
    print(result2)