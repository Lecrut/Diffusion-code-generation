import datetime

def get_january_1_day(year):
    date = datetime.date(year, 1, 1)
    return date.strftime("%A")

if __name__ == '__main__':
    result = get_january_1_day(2024)
    print(result)