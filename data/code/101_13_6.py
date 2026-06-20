import datetime

def get_weekday(date_str):
    day, month, year = map(int, date_str.split('-'))
    date_obj = datetime.date(year, month, day)
    day_of_week = date_obj.strftime("%A").upper()
    return day_of_week

if __name__ == '__main__':
    sample_date = "04-07-2024"
    weekday = get_weekday(sample_date)
    print(weekday)