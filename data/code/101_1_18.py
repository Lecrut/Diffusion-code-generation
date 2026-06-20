from calendar import weekday

def get_weekday_name(year, month, day):
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][weekday(year, month, day)]

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 26
    weekday_name = get_weekday_name(sample_year, sample_month, sample_day)
    print(weekday_name)