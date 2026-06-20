import datetime

def get_weekday(date_str):
    day_map = {
        0: "MONDAY",
        1: "TUESDAY",
        2: "WEDNESDAY",
        3: "THURSDAY",
        4: "FRIDAY",
        5: "SATURDAY",
        6: "SUNDAY"
    }
    day, month, year = map(int, date_str.split('-'))
    date_obj = datetime.date(year, month, day)
    weekday_num = date_obj.weekday()
    return day_map[weekday_num]

if __name__ == '__main__':
    sample_date = "04-07-2024"
    print(get_weekday(sample_date))