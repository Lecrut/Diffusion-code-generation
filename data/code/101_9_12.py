from datetime import datetime

def get_day_of_week(year, month, day):
    date = f"{year}-{month:02d}-{day:02d}"
    dt_object = datetime.strptime(date, "%Y-%m-%d")
    return dt_object.strftime("%A").upper()

if __name__ == '__main__':
    year = 2023
    month = 11
    day = 15
    print(get_day_of_week(year, month, day))