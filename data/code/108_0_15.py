import datetime

DAY_OF_MONTH = 15
MONTH = 10
YEAR = 2023

def get_day_of_month(year, month, day):
    date_obj = datetime.date(year, month, day)
    return date_obj.day

if __name__ == '__main__':
    print(get_day_of_month(YEAR, MONTH, DAY_OF_MONTH))