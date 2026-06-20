import datetime

def get_weekday(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        day_of_week = date_obj.strftime("%A").upper()
        return day_of_week
    except ValueError:
        raise ValueError("Invalid date components provided.")

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 7
    sample_day = 4
    weekday = get_weekday(sample_year, sample_month, sample_day)
    print(weekday)