import calendar

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_day_of_week(year, month, day):
    return DAYS_OF_WEEK[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    sample_date = (2023, 12, 25)
    print(f"The day of the week for {sample_date[1]}/{sample_date[0]} is {get_day_of_week(*sample_date)}.")