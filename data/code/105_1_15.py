import datetime

def first_sunday_after_jan_1():
    JAN_1_2024 = datetime.date(2024, 1, 1)
    while JAN_1_2024.weekday() != 6:
        JAN_1_2024 += datetime.timedelta(days=1)
    return JAN_1_2024

if __name__ == '__main__':
    print(first_sunday_after_jan_1())