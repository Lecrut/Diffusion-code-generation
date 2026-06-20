import datetime

def get_weekday(date_str):
    try:
        day, month, year = map(int, date_str.split('-'))
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime("%A").upper()
    except ValueError:
        raise ValueError("Invalid date components provided.")

if __name__ == '__main__':
    sample_date = "04-07-2024"
    weekday = get_weekday(sample_date)
    print(weekday)