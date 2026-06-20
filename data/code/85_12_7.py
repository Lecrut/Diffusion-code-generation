from datetime import datetime

def calculate_week_difference(date1, date2):
    time_difference = abs(date1 - date2)
    weeks = time_difference.days // 7
    return weeks

if __name__ == '__main__':
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 15)
    diff1 = calculate_week_difference(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {diff1} weeks")