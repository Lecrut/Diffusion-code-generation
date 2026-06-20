import datetime

def get_weekday(date_str):
    try:
        day, month, year = map(int, date_str.split('-'))
        date_obj = datetime.date(year, month, day)
        weekday = date_obj.strftime("%A")
        return weekday.upper()
    except ValueError:
        raise ValueError("Error: Invalid date components.")

if __name__ == '__main__':
    sample_date = "04-07-2024"
    print(get_weekday(sample_date))