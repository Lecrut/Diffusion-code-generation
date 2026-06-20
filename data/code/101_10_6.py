import calendar

def get_day_of_week(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    sample_date = (2023, 12, 25)
    day_of_week = get_day_of_week(*sample_date)
    print(f"The day of the week for {sample_date[1]}/{sample_date[0]} is {day_of_week}.")