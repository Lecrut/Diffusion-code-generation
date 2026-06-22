import datetime

def get_weekday(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    sample_date = "2023-12-25"
    weekday = get_weekday(sample_date)
    print(weekday)