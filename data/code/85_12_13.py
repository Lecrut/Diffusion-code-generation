from datetime import datetime

def calculate_week_difference(date1, date2):
    time_difference = abs(date2 - date1)
    weeks = time_difference.days // 7
    return weeks

if __name__ == '__main__':
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 15)
    date_c = datetime(2023, 6, 1)
    date_d = datetime(2023, 6, 20)

    diff_ab = calculate_week_difference(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {diff_ab} weeks")

    diff_cd = calculate_week_difference(date_c, date_d)
    print(f"Difference between {date_c.date()} and {date_d.date()}: {diff_cd} weeks")