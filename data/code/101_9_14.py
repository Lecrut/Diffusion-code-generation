from datetime import datetime

def get_day_of_week(date_str):
    date_format = "%Y-%m-%d"
    try:
        date_obj = datetime.strptime(date_str, date_format)
        day_of_week = date_obj.strftime("%A").upper()
        return day_of_week
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_date = '2023-11-11'
    print(get_day_of_week(sample_date))