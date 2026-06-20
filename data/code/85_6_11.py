def days_to_weeks(days):
    return days // 7

if __name__ == '__main__':
    date1 = 20231001
    date2 = 20231008
    diff_days = abs(date2 - date1)
    print(days_to_weeks(diff_days))