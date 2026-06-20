import datetime

def get_jan_1st_2024_day():
    date = datetime.date(2024, 1, 1)
    return date.strftime("%A")

if __name__ == '__main__':
    print(get_jan_1st_2024_day())