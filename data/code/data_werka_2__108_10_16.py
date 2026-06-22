import datetime

def get_day_of_week_for_january_1(year):
    date = datetime.date(year, 1, 1)
    return date.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week_for_january_1(2024)
    print(result)