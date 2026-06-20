from datetime import date, timedelta

def difference_in_weeks(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = date.strptime(date_str1, date_format)
    date2 = date.strptime(date_str2, date_format)
    time_difference = abs(date2 - date1)
    weeks = time_difference.days / 7
    return int(weeks)

if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2023-01-29"
    date_c = "2023-07-01"
    date_d = "2024-01-01"
    
    diff_ab = difference_in_weeks(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {diff_ab} weeks")
    
    diff_cd = difference_in_weeks(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {diff_cd} weeks")
    
    diff_ac = difference_in_weeks(date_a, date_c)
    print(f"Difference between {date_a} and {date_c}: {diff_ac} weeks")