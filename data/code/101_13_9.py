import datetime

def validate_date(day, month, year):
    try:
        return datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date components provided.")

def get_weekday(date_str):
    day, month, year = map(int, date_str.split('-'))
    date_obj = validate_date(day, month, year)
    return date_obj.strftime("%A").upper()

if __name__ == '__main__':
    sample_date = "04-07-2024"
    weekday = get_weekday(sample_date)
    print(weekday)