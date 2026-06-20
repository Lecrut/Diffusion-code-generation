from datetime import date, timedelta

def difference_in_weeks(date_str1, date_str2):
    format_str = "%Y-%m-%d"
    date1 = date.strptime(date_str1, format_str)
    date2 = date.strptime(date_str2, format_str)
    time_difference = abs(date1 - date2)
    weeks = time_difference.days / 7
    return int(weeks)

if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2023-01-29"
    date_c = "2024-01-01"
    diff_ab = difference_in_weeks(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {diff_ab} weeks")
    diff_ac = difference_in_weeks(date_a, date_c)
    print(f"Difference between {date_a} and {date_c}: {diff_ac} weeks")