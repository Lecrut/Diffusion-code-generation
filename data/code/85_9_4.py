from datetime import date
def date_difference_in_weeks(date1, date2):
    diff = abs(date1 - date2)
    diff_days = diff.days
    weeks = diff_days / 7.0
    return weeks
if __name__ == '__main__':
    d1 = date(2023, 1, 1)
    d2 = date(2023, 1, 10)
    result1 = date_difference_in_weeks(d1, d2)
    print(f"Difference between {d1} and {d2}: {result1} weeks")
    d3 = date(2022, 12, 31)
    d4 = date(2023, 1, 2)
    result2 = date_difference_in_weeks(d3, d4)
    print(f"Difference between {d3} and {d4}: {result2} weeks")
    d5 = date(2024, 5, 15)
    d6 = date(2023, 1, 1)
    result3 = date_difference_in_weeks(d5, d6)
    print(f"Difference between {d5} and {d6}: {result3} weeks")